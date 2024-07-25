from email.policy import default
from django.conf import settings
from typing_extensions import override
import openai


open_ai_key = settings.OPENAI_API_KEY

client = openai.OpenAI(api_key=open_ai_key)


class EventHandler(openai.AssistantEventHandler):
    def __init__(self):
        super().__init__()
        self.output_json = None

    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > ", end="", flush=True)

    @override
    def on_message_done(self, message) -> None:
        message_content = message.content[0].text # type: ignore
        annotations = message_content.annotations
        citations = []
        for index, annotation in enumerate(annotations):
            message_content.value = message_content.value.replace(
                annotation.text, f"[{index}]"
            )
            if file_citation := getattr(annotation, "file_citation", None):
                cited_file = client.files.retrieve(file_citation.file_id)
                citations.append(f"[{index}] {cited_file.filename}")
        print(message_content.value)
        print("\n".join(citations))
        
        # Extract JSON object from the response text
        json_start = message_content.value.find('{')
        json_end = message_content.value.rfind('}') + 1
        if json_start != -1 and json_end != -1:
            self.output_json = message_content.value[json_start:json_end]
        print("Output JSON captured:", self.output_json)