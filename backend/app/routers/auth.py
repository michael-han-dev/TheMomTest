from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import Optional
from ..services.supabase_client import get_supabase_client

router = APIRouter()

class UserSignUp(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    name: Optional[str] = None

class AuthResponse(BaseModel):
    user: UserResponse
    access_token: str
    refresh_token: str

@router.post("/signup", response_model=AuthResponse)
async def sign_up(user_data: UserSignUp):
    """
    Register a new user with email and password
    """
    supabase = get_supabase_client()
    
    try:
        # Register user with Supabase Auth
        auth_response = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password
        })
        
        # If registration successful, store additional user data
        if auth_response.user:
            # Add user to profiles table with additional data
            supabase.table("profiles").insert({
                "id": auth_response.user.id,
                "email": user_data.email,
                "name": user_data.name,
                "created_at": "now()"
            }).execute()
            
            # Return user data and tokens
            return AuthResponse(
                user=UserResponse(
                    id=auth_response.user.id,
                    email=auth_response.user.email,
                    name=user_data.name
                ),
                access_token=auth_response.session.access_token,
                refresh_token=auth_response.session.refresh_token
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create user"
            )
            
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating user: {str(e)}"
        )

@router.post("/login", response_model=AuthResponse)
async def login(user_data: UserLogin):
    """
    Log in an existing user with email and password
    """
    supabase = get_supabase_client()
    
    try:
        # Sign in user with Supabase Auth
        auth_response = supabase.auth.sign_in_with_password({
            "email": user_data.email,
            "password": user_data.password
        })
        
        # Get user profile data
        profile_response = supabase.table("profiles").select("*").eq("id", auth_response.user.id).execute()
        
        # Extract name from profile if available
        name = None
        if profile_response.data and len(profile_response.data) > 0:
            name = profile_response.data[0].get("name")
        
        # Return user data and tokens
        return AuthResponse(
            user=UserResponse(
                id=auth_response.user.id,
                email=auth_response.user.email,
                name=name
            ),
            access_token=auth_response.session.access_token,
            refresh_token=auth_response.session.refresh_token
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        ) 