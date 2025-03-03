from pydantic import BaseModel, Field
from typing import List, Optional

class StartupIdea(BaseModel):
    idea_name: str = Field(..., description="Name of the startup idea")
    problem_statement: str = Field(..., description="Description of the problem being solved")
    target_audience: str = Field(..., description="Description of the target audience")
    solution: str = Field(..., description="Description of the proposed solution")
    value_proposition: str = Field(..., description="Value proposition of the solution")

class InterviewQuestion(BaseModel):
    question: str = Field(..., description="The interview question")
    explanation: Optional[str] = Field(None, description="Explanation of why this question is effective")
    category: str = Field(..., description="Category of the question (e.g., problem validation, solution validation)")

class ValidationPlan(BaseModel):
    interview_questions: List[InterviewQuestion] = Field(..., description="List of interview questions")
    market_research_suggestions: List[str] = Field(..., description="Suggestions for market research")
    next_steps: List[str] = Field(..., description="Recommended next steps for validation")

class ValidationRequest(BaseModel):
    startup_idea: StartupIdea = Field(..., description="Details about the startup idea") 