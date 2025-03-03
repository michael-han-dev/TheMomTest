from app.models.validation import StartupIdea, ValidationPlan, InterviewQuestion
from typing import List

class ValidationService:
    """Service for generating validation plans based on startup ideas."""
    
    async def generate_validation_plan(self, startup_idea: StartupIdea) -> ValidationPlan:
        """
        Generate a validation plan for a startup idea.
        
        Args:
            startup_idea: The startup idea to validate
            
        Returns:
            A validation plan with interview questions and next steps
        """
        # In a real implementation, this would use OpenAI or another LLM to generate questions
        
        interview_questions = self._generate_interview_questions(startup_idea)
        market_research_suggestions = self._generate_market_research_suggestions(startup_idea)
        next_steps = self._generate_next_steps()
        
        return ValidationPlan(
            interview_questions=interview_questions,
            market_research_suggestions=market_research_suggestions,
            next_steps=next_steps
        )
    
    def _generate_interview_questions(self, startup_idea: StartupIdea) -> List[InterviewQuestion]:
        """Generate interview questions based on The Mom Test principles."""
        
        # These are example questions that follow The Mom Test principles
        questions = [
            InterviewQuestion(
                question=f"What's the hardest part about {startup_idea.problem_statement.split()[0:3]} in your day-to-day work?",
                explanation="Asks about their specific problems without mentioning your solution",
                category="problem validation"
            ),
            InterviewQuestion(
                question="Can you walk me through the last time you encountered this problem?",
                explanation="Gets specific examples rather than hypotheticals",
                category="problem validation"
            ),
            InterviewQuestion(
                question="What solutions have you tried before? What worked and what didn't?",
                explanation="Uncovers existing alternatives and their shortcomings",
                category="solution validation"
            ),
            InterviewQuestion(
                question="How much time/money do you currently spend dealing with this issue?",
                explanation="Quantifies the problem to understand its importance",
                category="problem validation"
            ),
            InterviewQuestion(
                question="How are you currently solving this problem?",
                explanation="Reveals if they're actively seeking solutions or if it's not a priority",
                category="solution validation"
            ),
        ]
        
        return questions
    
    def _generate_market_research_suggestions(self, startup_idea: StartupIdea) -> List[str]:
        """Generate market research suggestions."""
        
        return [
            "Research relevant Reddit communities",
            "Follow industry experts and potential customers on Twitter",
            "Check similar products on Product Hunt and their reviews",
            "Join industry forums and communities"
        ]
    
    def _generate_next_steps(self) -> List[str]:
        """Generate next steps for validation."""
        
        return [
            "Conduct customer interviews using the questions above",
            "Record and analyze the responses",
            "Identify patterns and pain points",
            "Return to this platform to analyze your findings"
        ]

# Create a singleton instance
validation_service = ValidationService() 