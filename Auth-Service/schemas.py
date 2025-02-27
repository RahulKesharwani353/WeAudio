from pydantic import BaseModel, Field
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = True

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "mohan",
                "email": "mohan@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }
    }

class Settings(BaseModel):
    authjwt_secret_key: str = 'b4bb9013c1c03b29b9311ec0df07f3b0d8fd13edd02d5c45b2fa7b86341fa405'

class LoginModel(BaseModel):
    username: str
    password: str