# Project-Backend-AI-Generator

## Overview
Project-Backend-AI-Generator is a backend application designed to generate project structures, code, and test cases based on user-provided requirements in a DOCX file. It leverages FastAPI for API development and integrates with LangChain for document processing and AI-driven code generation.

## Features
- Upload DOCX files to extract project requirements.
- Automatically generate backend code, including API endpoints, database models, and test cases.
- Supports folder structure generation based on predefined templates.
- Provides a downloadable ZIP file containing the generated project.

## Technologies Used
- **FastAPI**: For building the backend APIs.
- **LangChain**: For AI-driven document analysis and code generation.
- **SQLAlchemy**: For database modeling and ORM.
- **Python-Dotenv**: For environment variable management.
- **Docx2txt**: For extracting text from DOCX files.

- ## `uploadDoc.py`

### Overview
The `uploadDoc.py` file defines an API route for handling file uploads. It processes a DOCX file uploaded by the user, extracts its content, generates backend code based on the extracted data, and provides a downloadable ZIP file containing the generated project.

### Features
- Accepts a DOCX file upload via the `/upload/` endpoint.
- Invokes the `generateCode.py` script to process the uploaded file and generate the project.
- Returns a ZIP file (`generated_project.zip`) containing the generated project structure and code.

### Endpoint
#### `POST /upload/`
- **Description**: Uploads a DOCX file, processes it, and returns a ZIP file with the generated project.
- **Request**:
  - File: A DOCX file (`application/vnd.openxmlformats-officedocument.wordprocessingml.document`).
- **Response**:
  - Status Code: `201 Created`
  - Content: A downloadable ZIP file (`generated_project.zip`).

### Code Explanation
- **Imports**:
  - `APIRouter`, `File`, `UploadFile`, `status`: FastAPI components for defining routes and handling file uploads.
  - `FileResponse`: Used to send the generated ZIP file as a response.
  - `fetched_code`: An instance of the `getBackendData` class from `generateCode.py`, which handles the code generation process.
  
- **Router**:
  - The `APIRouter` instance is used to define the `/upload/` endpoint.

- **Functionality**:
  - The `create_upload_file` function:
    1. Reads the uploaded DOCX file.
    2. Passes the file content to the `fetched_code.run()` method for processing.
    3. Returns the generated ZIP file (`generated_project.zip`) as a response.

