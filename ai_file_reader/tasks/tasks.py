import os
import json
from celery import shared_task
from django.conf import settings
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain.chains.openai_tools import create_extraction_chain_pydantic
from pydantic import BaseModel

from ..form_data_type import FormDataType  # Pydantic model
from ..prompts import get_chemical_intake_prompt
from ..storage import TemporaryFileStorage


def _normalize_result(value):
    if isinstance(value, BaseModel):
        return value.model_dump()
    if isinstance(value, list):
        return [_normalize_result(item) for item in value]
    if isinstance(value, dict):
        return {key: _normalize_result(item) for key, item in value.items()}
    return value


@shared_task(bind=True)
def process_uploaded_files_task(self, file_names, task_id):
    temp_storage = TemporaryFileStorage()
    file_chunks = []

    try:
        if not file_names:
            return {}

        # Load and chunk each uploaded PDF
        for file_name in file_names:
            file_path = temp_storage.path(file_name)
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = splitter.split_documents(documents)
            file_chunks.extend(chunks)

        # Setup LangChain LLM and prompt
        model_name = getattr(settings, "AI_READER_MODEL", "gpt-4o-mini")
        llm = ChatOpenAI(model=model_name, temperature=0)

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

        return _normalize_result(result)

    except Exception as e:
        self.retry(exc=e, countdown=60, max_retries=3)
        raise

    finally:
        for file_name in file_names:
            try:
                temp_storage.delete(file_name)
            except Exception:
                pass
