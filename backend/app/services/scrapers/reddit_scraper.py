import os
import praw
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from ...routers.research import ResearchResult

# Load environment variables
load_dotenv()

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "TheMomTestBot/1.0")

# Initialize Reddit client
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

async def search(query: str, max_results: int = 50) -> List[ResearchResult]:
    """
    Search Reddit for posts and comments matching the query.
    
    Args:
        query: The search query
        max_results: Maximum number of results to return
        
    Returns:
        List of ResearchResult objects
    """
    try:
        # In a real implementation, this would use the Reddit API
        # For now, we'll return mock data
        
        # Example of how you would call the Reddit API in a real implementation:
        """
        results = []
        
        # Search for submissions
        for submission in reddit.subreddit("all").search(query, limit=max_results//2):
            results.append(ResearchResult(
                platform="reddit",
                source_url=f"https://www.reddit.com{submission.permalink}",
                content=submission.title + "\n\n" + submission.selftext,
                author=submission.author.name if submission.author else "[deleted]",
                date=datetime.fromtimestamp(submission.created_utc).isoformat(),
                engagement={
                    "upvotes": submission.score,
                    "comments": submission.num_comments
                },
                sentiment=None  # Would be analyzed separately
            ))
            
        # Search for comments
        for comment in reddit.subreddit("all").comments(limit=max_results//2):
            if query.lower() in comment.body.lower():
                results.append(ResearchResult(
                    platform="reddit",
                    source_url=f"https://www.reddit.com{comment.permalink}",
                    content=comment.body,
                    author=comment.author.name if comment.author else "[deleted]",
                    date=datetime.fromtimestamp(comment.created_utc).isoformat(),
                    engagement={
                        "upvotes": comment.score
                    },
                    sentiment=None  # Would be analyzed separately
                ))
        """
        
        # Mock data for demonstration
        results = [
            ResearchResult(
                platform="reddit",
                source_url="https://www.reddit.com/r/startups/comments/123456/dealing_with_problem",
                content=f"[Advice Needed] How do you deal with {query}?\n\nI've been struggling with this for my startup and would appreciate any advice from those who've overcome this challenge.",
                author="startup_founder123",
                date="2023-01-20T10:25:00Z",
                engagement={
                    "upvotes": 78,
                    "comments": 32
                },
                sentiment="neutral"
            ),
            ResearchResult(
                platform="reddit",
                source_url="https://www.reddit.com/r/Entrepreneur/comments/789012/success_story",
                content=f"How I solved {query} and grew my business 3x\n\nAfter months of struggling, I finally found a solution that worked for me. Here's my journey...",
                author="successful_entrepreneur",
                date="2023-01-18T16:40:00Z",
                engagement={
                    "upvotes": 215,
                    "comments": 47
                },
                sentiment="positive"
            ),
            ResearchResult(
                platform="reddit",
                source_url="https://www.reddit.com/r/SaaS/comments/345678/comment/abc123",
                content=f"The problem with most solutions for {query} is that they're built by engineers who don't understand the actual business needs. What we really need is...",
                author="saas_veteran",
                date="2023-01-12T08:15:00Z",
                engagement={
                    "upvotes": 42
                },
                sentiment="negative"
            )
        ]
        
        return results
        
    except Exception as e:
        print(f"Error searching Reddit: {str(e)}")
        return [] 