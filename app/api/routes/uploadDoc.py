import os
from fastapi import APIRouter, File, UploadFile, status, HTTPException
from fastapi.responses import FileResponse
from scripts.generateCode import fetched_code

router = APIRouter()

@router.post("/upload/", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile = File(...)):
    content = await file.read()
    zip_file_path = "generated_project.zip"
    max_attempts = 5

    for attempt in range(max_attempts):
        fetched_code.run(content)
        print("Attempt:", attempt + 1)
        if os.path.exists(zip_file_path):
            break
    else:
        # Handle the case when the file still doesn't exist after max attempts
        raise HTTPException(status_code=500, detail="Failed to generate project zip after {} attempts".format(max_attempts))

    return FileResponse(path=zip_file_path, media_type="application/zip", filename="generated_project.zip")
