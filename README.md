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
