import json
from django.test import TestCase

# Create your tests here.
from ai_file_reader.tasks import process_uploaded_files_task

# path to a local SDS PDF
sds_pdf_path = "~/Users/gabrielodame/Downloads/lactic_acid_-_88_sds.pdf"

# run the task synchronously (not as background job)
result = process_uploaded_files_task.run([sds_pdf_path], "test-task-id")

# print result
print(json.dumps(result, indent=2))
