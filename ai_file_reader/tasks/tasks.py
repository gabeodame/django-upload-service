import os
import json
from celery import shared_task
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain.chains.openai_tools import create_extraction_chain_pydantic

from ..form_data_type import FormDataType  # Pydantic model
from ..prompts import get_chemical_intake_prompt
from ..storage import TemporaryFileStorage

@shared_task(bind=True)
def process_uploaded_files_task(self, file_paths, task_id):
    temp_storage = TemporaryFileStorage()
    file_chunks = []

    try:
        # Load and chunk each uploaded PDF
        for file_path in file_paths:
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = splitter.split_documents(documents)
            file_chunks.extend(chunks)

        # Setup LangChain LLM and prompt
        llm = ChatOpenAI(model="gpt-4o", temperature=0)

        # Replace previous prompt with your detailed instruction prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert SDS extractor."),
            ("human", get_chemical_intake_prompt())
        ])

        chain = create_extraction_chain_pydantic(
            pydantic_schema=FormDataType,
            llm=llm,
            prompt=prompt
        )

        # Join all chunks into one large text block for input
        full_input = "\n\n".join([chunk.page_content for chunk in file_chunks])

        # Run LangChain extraction
        result = chain.invoke({"input": full_input})

        return json.loads(result.json())

    except Exception as e:
        self.retry(exc=e, countdown=60, max_retries=3)
        raise

    finally:
        for file_path in file_paths:
            try:
                temp_storage.delete(file_path)
            except Exception:
                pass
