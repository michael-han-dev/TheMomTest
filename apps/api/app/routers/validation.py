from fastapi import APIRouter, Depends, HTTPException
from app.models.validation import ValidationRequest, ValidationPlan
from app.services.validation_service import validation_service

router = APIRouter()

@router.post("/generate-plan", response_model=ValidationPlan)
async def generate_validation_plan(request: ValidationRequest):
    """
    Generate a validation plan for a startup idea based on The Mom Test principles.
    
    This endpoint takes a startup idea and returns a validation plan with:
    - Interview questions that follow The Mom Test principles
    - Market research suggestions
    - Next steps for validation
    """
    try:
        validation_plan = await validation_service.generate_validation_plan(request.startup_idea)
        return validation_plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate validation plan: {str(e)}") 