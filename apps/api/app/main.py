from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import validation, auth

app = FastAPI(
    title="The Mom Test Bot API",
    description="API for validating startup ideas using principles from The Mom Test",
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
app.include_router(validation.router, prefix="/api/validation", tags=["validation"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "API is running"} 