from fastapi import APIRouter, File, UploadFile, status
from fastapi.responses import FileResponse
from scripts.generateCode import fetched_code

router = APIRouter()

@router.post("/upload/", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile = File(...)):
    content = await file.read()
    fetched_code.run(content)
    zip_file_path = "generated_project.zip"
    return FileResponse(path=zip_file_path, media_type="application/zip", filename="generated_project.zip")
