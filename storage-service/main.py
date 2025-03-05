from fastapi import Depends, FastAPI, Security, APIRouter, status, Depends, HTTPException, File, UploadFile
from fastapi.routing import APIRoute, jsonable_encoder
from fastapi.security import HTTPBearer, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.openapi.utils import get_openapi
from utils import upload

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

app.include_router(router)