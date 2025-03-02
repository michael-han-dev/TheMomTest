# The Mom Test Bot

A web application that helps entrepreneurs validate their startup ideas using principles from "The Mom Test" by Rob Fitzpatrick. This platform guides users through the process of properly validating their ideas by ensuring they ask the right questions and gather meaningful feedback.

## Project Overview

The Mom Test Bot combines:
- **Idea Validation Framework**: Based on principles from "The Mom Test" book
- **Guided User Interviews**: Templates and guidance for conducting effective customer interviews
- **Web Research Pipeline**: Automated research on platforms like Twitter, Reddit, and Quora to gather market insights
- **AI-Powered Analysis**: Evaluation of user interviews and research data

## Tech Stack

### Frontend
- Next.js (React framework)
- TypeScript
- TailwindCSS for styling
- Supabase Auth for user authentication

### Backend
- FastAPI (Python) for the research pipeline and AI analysis
- Supabase for database and authentication

### AI/ML
- Custom trained model on "The Mom Test" principles
- Web scraping and analysis pipeline

## Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.9+)
- Supabase account

### Frontend Setup
```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn main:app --reload
```

### Environment Variables
Create a `.env.local` file in the root directory with the following variables:
```
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```