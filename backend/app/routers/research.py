from fastapi import APIRouter, HTTPException, Depends, status, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from ..services.supabase_client import get_supabase_client
from ..services.scrapers import twitter_scraper, reddit_scraper, quora_scraper
from ..services.research_analyzer import analyze_research_data

router = APIRouter()

class ResearchQuery(BaseModel):
    query: str
    platforms: List[str]
    max_results: Optional[int] = 50

class ResearchResult(BaseModel):
    platform: str
    source_url: str
    content: str
    author: Optional[str] = None
    date: Optional[str] = None
    engagement: Optional[Dict[str, Any]] = None
    sentiment: Optional[str] = None

class ResearchResponse(BaseModel):
    results: List[ResearchResult]
    analysis: Dict[str, Any]
    summary: str

@router.post("/search", response_model=ResearchResponse)
async def search_platforms(query: ResearchQuery, background_tasks: BackgroundTasks):
    """
    Search across multiple platforms (Twitter, Reddit, Quora) for relevant content
    related to the query and analyze the results.
    """
    try:
        results = []
        
        # Search across selected platforms
        if "twitter" in query.platforms:
            twitter_results = await twitter_scraper.search(query.query, max_results=query.max_results)
            results.extend(twitter_results)
            
        if "reddit" in query.platforms:
            reddit_results = await reddit_scraper.search(query.query, max_results=query.max_results)
            results.extend(reddit_results)
            
        if "quora" in query.platforms:
            quora_results = await quora_scraper.search(query.query, max_results=query.max_results)
            results.extend(quora_results)
        
        # Analyze the research data
        analysis, summary = analyze_research_data(results)
        
        # Store results in background (don't wait for completion)
        background_tasks.add_task(
            store_research_results,
            query=query.query,
            results=results,
            analysis=analysis
        )
        
        return ResearchResponse(
            results=results,
            analysis=analysis,
            summary=summary
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error performing research: {str(e)}"
        )

async def store_research_results(query: str, results: List[ResearchResult], analysis: Dict[str, Any]):
    """Store research results in the database"""
    supabase = get_supabase_client()
    
    # Store in Supabase
    try:
        supabase.table("research_results").insert({
            "query": query,
            "results": results,
            "analysis": analysis,
            "created_at": "now()"
        }).execute()
    except Exception as e:
        print(f"Error storing research results: {str(e)}")
        # Log error but don't fail the request 