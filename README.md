# Django Upload Service Application

This project is a Django-based file upload and processing service designed to handle various file types, support metadata extraction, and integrate AI-powered file analysis. It is structured for scalability and includes support for file uploads, secure storage, metadata management, and AI-driven insights.

---

## Features

- **File Uploads**:
  - Upload files to categorized directories based on type.
  - Supports metadata extraction and database storage for file details.

- **File Retrieval**:
  - Serve files by ID with appropriate MIME types.
  - Retrieve file metadata via API.

- **AI-Powered Analysis**:
  - Integrates with OpenAI API for file processing and chemical review.
  - Uses vector stores for efficient file metadata storage and search.

- **Authentication**:
  - JWT-based login with access and refresh tokens.
  - User authentication for secure API access.

- **Debugging Utilities**:
  - IIS-specific request metadata logging for troubleshooting.
  - CORS preflight endpoint for cross-origin requests.

---

## Prerequisites

1. **Environment Setup**:
   - Python 3.8+
   - Django 5.0
   - Django REST Framework
   - `rest_framework_simplejwt` for JWT authentication.

2. **Required Libraries**:
   - `openai`
   - `django-cors-headers`
   - Any other libraries listed in the `requirements.txt`.

3. **Configurations**:
   - Set up `settings.py` for:
     - `MEDIA_ROOT` and `MEDIA_URL` for file storage.
     - OpenAI API key (`OPENAI_API_KEY`).

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Endpoints

### Public Endpoints
| **URL**                             | **Method** | **Description**                                   |
|-------------------------------------|------------|---------------------------------------------------|
| `/`                                 | GET        | Displays the home page.                          |
| `/files/`                           | GET        | Lists all uploaded files.                        |
| `/files/<int:file_id>/`             | GET        | Serves a file by its ID.                         |
| `/files/details/<int:file_id>/`     | GET        | Fetches metadata for a specific file.            |
| `/uploads/<folder>/<brand_name>/<kind>/` | POST   | Uploads a file (without date).                   |
| `/uploads/<folder>/<brand_name>/<date>/<kind>/` | POST | Uploads a file with a specified date.            |

### Authentication Endpoints
| **URL**         | **Method** | **Description**            |
|------------------|------------|----------------------------|
| `/api/login/`    | POST       | Logs in and returns tokens.|

### AI File Reader Endpoint
| **URL**                    | **Method** | **Description**                          |
|-----------------------------|------------|------------------------------------------|
| `/ai-file-reader/`          | POST       | Processes uploaded files using AI tools. |

---

## Project Structure

```
rduploadservice/
│
├── uploadservice/
│   ├── views.py         # Core logic for file uploads and serving.
│   ├── models.py        # Database models for file metadata.
│   ├── serializers.py   # DRF serializers for API responses.
│   ├── urls.py          # Endpoint configurations.
│   └── templates/       # HTML templates for rendering pages.
│
├── ai_file_reader/
│   ├── views.py         # AI file reader integration.
│   ├── storage.py       # Temporary file storage management.
│   ├── event_handler.py # AI event handling logic.
│   ├── prompts.py       # AI assistant prompts.
│
├── settings.py           # Django project settings.
├── urls.py               # Main URL routing.
├── requirements.txt      # Python dependencies.
└── README.md             # Project documentation.
```

---

## Usage

### Uploading Files
Use the `/uploads/<folder>/<brand_name>/<kind>/` endpoint to upload files. Files are stored in categorized directories, and metadata is saved to the database.

### Accessing Files
Files can be accessed using `/files/<int:file_id>/`. Metadata can be retrieved with `/files/details/<int:file_id>/`.

### AI-Powered Analysis
Send files to the `/ai-file-reader/` endpoint for chemical review and product insights powered by OpenAI.

---

## Notes

- **Security**: Ensure your OpenAI API key and sensitive credentials are not exposed in version control.
- **Testing**: Add unit tests for endpoints and edge cases using Django's testing framework.
- **Scalability**: Consider optimizing file storage with cloud services like AWS S3 or Azure Blob Storage.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
