import json
import openai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .storage import TemporaryFileStorage
from .event_handler import EventHandler
from .prompts import get_chemical_intake_prompt

# Initialize OpenAI API Key
openai.api_key = settings.OPENAI_API_KEY

# Temporary file storage for uploaded files
temp_storage = TemporaryFileStorage()

@csrf_exempt
def process_files(request):
    if request.method == 'POST':
        if 'files' not in request.FILES:
            return JsonResponse({'error': 'No files provided'}, status=400)

        uploaded_files = request.FILES.getlist('files')
        file_paths = []
        file_streams = []
        event_handler = EventHandler()

        try:
            # Save uploaded files temporarily
            for uploaded_file in uploaded_files:
                file_name = temp_storage.save(uploaded_file.name, uploaded_file)
                file_path = temp_storage.path(file_name)
                file_paths.append(file_path)
                file_streams.append(open(file_path, 'rb'))

            # Initialize OpenAI client
            client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

            # Debug: Print the prompt
            prompt_content = get_chemical_intake_prompt()
            print(f"Prompt content: {prompt_content}")

            # Step 3: Create vector store to store file metadata
            vector_store = client.beta.vector_stores.create(name="Chemical Review", expires_after={
                "anchor": "last_active_at",
                "days": 1
            })

            # Upload files to the OpenAI vector store
            file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store.id, files=file_streams
            )

            # Debug: Ensure files are uploaded correctly by checking file counts
            print(f"File batch uploaded successfully, file count: {file_batch.file_counts}")

            # Step 4: Create the assistant and set the tool for file search
            assistant = client.beta.assistants.create(
                name='R&D Scientist and Product Developer',
                instructions=(
                    "You are an expert product developer specializing in household, institutional, and healthcare products. "
                    "Your role involves reviewing chemical documents such as Safety Data Sheets (SDS) and Technical Data Sheets (TDS) "
                    "to provide insights for developing sustainable and high-performing products. "
                    "Additionally, you are responsible for generating accurate and thorough product specifications."
                ),
                model='gpt-4-turbo',
                tools=[{"type": "file_search"}],  # Use the correct tool
                tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
            )

            # Debug: Print the assistant ID
            print(f"Assistant ID: {assistant.id}")

            # Step 5: Prepare the files to be processed by the assistant
            message_files = [
                client.files.create(file=open(file_path, "rb"), purpose="assistants")
                for file_path in file_paths
            ]

            # Debug: Print file IDs for confirmation
            for message_file in message_files:
                print(f"File ID: {message_file.id}, Filename: {message_file.filename}")

            # Step 6: Create the thread and submit the prompt and file references
            thread = client.beta.threads.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt_content,
                        "attachments": [
                            {
                                "file_id": message_file.id, 
                                "tools": [{"type": "file_search"}]  # Correctly referencing the file search tool
                            }
                            for message_file in message_files
                        ]
                    }
                ]
            )

            # Debug: Print the thread ID for tracking
            print(f"Thread ID: {thread.id}")

            # Step 7: Poll the thread run and wait for the result
            run = client.beta.threads.runs.create_and_poll(
                thread_id=thread.id, assistant_id=assistant.id
            )

            # Step 8: Fetch messages from the thread
            messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

            # Handle empty messages scenario
            if not messages:
                print("No messages returned from the assistant.")
                return JsonResponse({'error': 'No messages returned from the assistant. Please check the input files and prompt.'}, status=500)

            # Process messages with EventHandler
            output_data = event_handler.process_messages(messages, client)

            # Check if there is an error in the output data
            if 'error' in output_data:
                return JsonResponse(output_data, status=500)
            else:
                return JsonResponse(output_data, safe=False)

        except Exception as e:
            # Clean up file streams and temporary files on error
            for file_stream in file_streams:
                file_stream.close()

            for file_path in file_paths:
                try:
                    temp_storage.delete(file_path)
                except Exception as delete_error:
                    print(f"Error deleting file {file_path}: {delete_error}")

            print("Error occurred:", str(e))
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
