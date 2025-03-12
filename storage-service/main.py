from fastapi import Depends, FastAPI, Security, APIRouter, status, BackgroundTasks, HTTPException, File, UploadFile
from fastapi.routing import APIRoute, jsonable_encoder
from fastapi.security import HTTPBearer, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.openapi.utils import get_openapi
from utils import upload, download
from fastapi.responses import FileResponse, StreamingResponse
import tempfile, os

from dotenv import load_dotenv
load_dotenv()

app=FastAPI(
        title="User Management API",
    description="API for user registration and management",
    version="1.0.0"
)


router = APIRouter(
    prefix='/file',
    tags=['file']
)

@router.get('/')
async def hello():
    """
    ## Sample hello world route
    """
    return {"message": "Hello World"}

# Add Posty Request to upload a video
@router.post('/upload')
async def upload_video(
    video: UploadFile = File(...)
):
    """
    ## Upload a video
    """
    if not video.content_type.startswith('video/'):
        raise HTTPException(status_code=400, detail="File must be a video")
    contents = await video.read()

    response, status = await upload.upload(contents)
    
    return response

@router.get('/download/{file_id}')
async def download_audio(file_id: str, background_tasks: BackgroundTasks):
    """
    ## Download the converted audio file
    """

    file, status = await download.download(file_id)
    if status != 200:
        raise HTTPException(status_code=status, detail=file)
    
    async def file_streamer():
        chunk = await file.read(1024 * 10)
        while chunk:
            yield chunk
            chunk = await file.read(1024 * 10)
    
    headers = {"Content-Disposition": f"attachment; filename={file_id}.mp3"}
    return StreamingResponse(file_streamer(), media_type='audio/mpeg', headers=headers)

app.include_router(router)