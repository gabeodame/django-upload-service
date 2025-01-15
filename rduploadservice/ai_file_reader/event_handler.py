from django.conf import settings
from typing_extensions import override
import openai

open_ai_key = settings.OPENAI_API_KEY
client = openai.OpenAI(api_key=open_ai_key)

class EventHandler:
    def __init__(self):
        self.output_json = None

    def get_output_json(self):
        return self.output_json

    def process_messages(self, messages, client):
        try:
            if not messages:
                return {'error': 'No messages returned'}
            
            message_content = messages[0].content[0].text  # Get the first message text
            annotations = message_content.annotations
            citations = []
            
            for index, annotation in enumerate(annotations):
                message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
                if file_citation := getattr(annotation, "file_citation", None):
                    cited_file = client.files.retrieve(file_citation.file_id)
                    citations.append(f"[{index}] {cited_file.filename}")

            return {
                'message': message_content.value,
                'citations': citations
            }

        except Exception as e:
            return {'error': str(e)}