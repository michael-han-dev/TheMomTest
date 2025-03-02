import os
from typing import List, Dict, Any
from dotenv import load_dotenv
import openai
from ..routers.validation import InterviewQuestion

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_idea(
    idea_name: str,
    problem_statement: str,
    target_audience: str,
    solution: str,
    value_proposition: str
) -> Dict[str, Any]:
    """
    Analyze a startup idea using The Mom Test principles.
    
    Returns a dictionary with analysis results.
    """
    # In a real implementation, this would use OpenAI or a custom-trained model
    # For now, we'll return a mock analysis
    
    # Example of how you would call OpenAI in a real implementation:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in startup idea validation using The Mom Test principles."},
            {"role": "user", "content": f"Analyze this startup idea:\nName: {idea_name}\nProblem: {problem_statement}\nTarget Audience: {target_audience}\nSolution: {solution}\nValue Proposition: {value_proposition}"}
        ]
    )
    analysis_text = response.choices[0].message.content
    """
    
    # Mock analysis for demonstration
    analysis = {
        "overall_score": 7.5,
        "strengths": [
            "Clear problem statement",
            "Well-defined target audience"
        ],
        "weaknesses": [
            "Value proposition could be more specific",
            "Solution may be too broad"
        ],
        "mom_test_violations": [
            "The problem statement contains some assumptions that should be validated",
            "The solution assumes users will change their behavior"
        ],
        "validation_priorities": [
            "Verify that the target audience actually experiences this problem",
            "Determine if they're actively seeking solutions",
            "Find out what they've already tried"
        ]
    }
    
    return analysis

def generate_interview_questions(
    problem_area: str,
    target_audience: str
) -> List[InterviewQuestion]:
    """
    Generate interview questions based on The Mom Test principles.
    
    Returns a list of InterviewQuestion objects.
    """
    # In a real implementation, this would use OpenAI or a custom-trained model
    # For now, we'll return mock questions
    
    # Example of how you would call OpenAI in a real implementation:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in The Mom Test methodology for startup validation."},
            {"role": "user", "content": f"Generate 5 interview questions following The Mom Test principles for validating a solution to this problem: {problem_area} for this target audience: {target_audience}"}
        ]
    )
    questions_text = response.choices[0].message.content
    """
    
    # Mock questions for demonstration
    questions = [
        InterviewQuestion(
            question="Can you tell me about the last time you encountered [problem area]?",
            explanation="This asks for a specific story rather than a generalization, revealing how they actually behave.",
            category="Past Behavior"
        ),
        InterviewQuestion(
            question="What have you already tried to solve this problem?",
            explanation="Reveals existing solutions they've considered and whether they're actively trying to solve it.",
            category="Solution Exploration"
        ),
        InterviewQuestion(
            question="How are you dealing with this issue today?",
            explanation="Uncovers current workarounds and the severity of the problem.",
            category="Current Process"
        ),
        InterviewQuestion(
            question="How much time/money do you currently spend on this problem?",
            explanation="Quantifies the problem's impact and potential budget for a solution.",
            category="Problem Impact"
        ),
        InterviewQuestion(
            question="What would an ideal solution look like to you?",
            explanation="Lets them describe their needs without biasing them toward your specific solution.",
            category="Needs Assessment"
        )
    ]
    
    return questions 