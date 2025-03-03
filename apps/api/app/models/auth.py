from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., description="User's password", min_length=8)
    name: Optional[str] = Field(None, description="User's full name")

class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., description="User's password")

class Token(BaseModel):
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(..., description="Token type")

class TokenData(BaseModel):
    email: Optional[str] = None
    user_id: Optional[str] = None

class User(BaseModel):
    id: str = Field(..., description="User ID")
    email: EmailStr = Field(..., description="User's email address")
    name: Optional[str] = Field(None, description="User's full name")
    is_active: bool = Field(True, description="Whether the user is active") 