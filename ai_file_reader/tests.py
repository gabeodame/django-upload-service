import tempfile
from uuid import uuid4
from unittest.mock import Mock, patch

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, SimpleTestCase, override_settings


class ProcessFilesTests(SimpleTestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

    @override_settings(TEMP_MEDIA_ROOT=None)
    def test_process_files_dispatches_task(self):
        with override_settings(TEMP_MEDIA_ROOT=self.temp_dir.name):
            uploaded = SimpleUploadedFile(
                "sample.pdf",
                b"%PDF-1.4 test",
                content_type="application/pdf",
            )

            with patch("ai_file_reader.views.process_uploaded_files_task.delay") as delay_mock:
                response = self.client.post(
                    "/ai-file-reader/process-files/",
                    {"files": [uploaded]},
                )

            self.assertEqual(response.status_code, 202)
            payload = response.json()
            self.assertIn("task_id", payload)
            delay_mock.assert_called_once()
            args, _ = delay_mock.call_args
            self.assertEqual(args[1], payload["task_id"])
            self.assertIsInstance(args[0], list)


class TaskStatusTests(SimpleTestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()

    @patch("ai_file_reader.tasks.task_status_view.AsyncResult")
    def test_task_status_success(self, async_result_mock):
        task_id = uuid4()
        result_mock = Mock()
        result_mock.status = "SUCCESS"
        result_mock.successful.return_value = True
        result_mock.failed.return_value = False
        result_mock.result = {"ok": True}
        async_result_mock.return_value = result_mock

        response = self.client.get(f"/ai-file-reader/api/tasks/{task_id}/status/")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["status"], "SUCCESS")
        self.assertEqual(payload["result"], {"ok": True})

    @patch("ai_file_reader.tasks.task_status_view.AsyncResult")
    def test_task_status_failure(self, async_result_mock):
        task_id = uuid4()
        result_mock = Mock()
        result_mock.status = "FAILURE"
        result_mock.successful.return_value = False
        result_mock.failed.return_value = True
        result_mock.result = RuntimeError("boom")
        async_result_mock.return_value = result_mock

        response = self.client.get(f"/ai-file-reader/api/tasks/{task_id}/status/")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["status"], "FAILURE")
        self.assertIn("error", payload)
