from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from ..services.supabase_client import get_supabase_client
from ..services.mom_test_analyzer import analyze_idea, generate_interview_questions

router = APIRouter()

class IdeaInput(BaseModel):
    idea_name: str
    problem_statement: str
    target_audience: str
    solution: str
    value_proposition: str

class InterviewQuestion(BaseModel):
    question: str
    explanation: str
    category: str

class ValidationResponse(BaseModel):
    interview_questions: List[InterviewQuestion]
    analysis: Dict[str, Any]
    recommendations: List[str]
    research_topics: List[str]

@router.post("/analyze", response_model=ValidationResponse)
async def validate_idea(idea: IdeaInput):
    """
    Analyze a startup idea using The Mom Test principles and generate
    appropriate interview questions and recommendations.
    """
    try:
        # Analyze the idea based on Mom Test principles
        analysis = analyze_idea(
            idea_name=idea.idea_name,
            problem_statement=idea.problem_statement,
            target_audience=idea.target_audience,
            solution=idea.solution,
            value_proposition=idea.value_proposition
        )
        
        # Generate interview questions
        interview_questions = generate_interview_questions(
            problem_area=idea.problem_statement,
            target_audience=idea.target_audience
        )
        
        # Generate research topics based on the idea
        research_topics = [
            f"{idea.target_audience} problems with {idea.problem_statement}",
            f"alternatives to {idea.solution}",
            f"why {idea.target_audience} don't use existing solutions",
            f"{idea.target_audience} communities online"
        ]
        
        # Generate recommendations
        recommendations = [
            "Conduct at least 10 customer interviews using the provided questions",
            "Focus on learning about their problems, not pitching your solution",
            "Look for specific examples of how they've tried to solve this problem before",
            "Pay attention to emotional responses and strong reactions",
            "Ask about their current spending on related solutions"
        ]
        
        return ValidationResponse(
            interview_questions=interview_questions,
            analysis=analysis,
            recommendations=recommendations,
            research_topics=research_topics
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error analyzing idea: {str(e)}"
        ) 