from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os
from dotenv import load_dotenv

# Import our modules
from app.routers import validation, research, auth
from app.services.supabase_client import get_supabase_client

# Load environment variables
load_dotenv()

app = FastAPI(
    title="The Mom Test Bot API",
    description="API for validating startup ideas using The Mom Test principles",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(validation.router, prefix="/validation", tags=["Validation"])
app.include_router(research.router, prefix="/research", tags=["Research"])

@app.get("/")
async def root():
    return {"message": "Welcome to The Mom Test Bot API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)