# The Mom Test Bot API

This is the FastAPI backend for The Mom Test Bot, a web application that helps entrepreneurs validate their startup ideas using principles from "The Mom Test" by Rob Fitzpatrick.

## Features

- Generate validation plans for startup ideas
- Create interview questions based on The Mom Test principles
- User authentication and authorization
- Integration with OpenAI for AI-powered validation

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
2. Navigate to the API directory:
   ```
   cd apps/api
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Copy the example environment file:
   ```
   cp .env.example .env
   ```
7. Edit the `.env` file with your configuration

### Running the API

```
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000.

### API Documentation

Once the API is running, you can access the Swagger documentation at:

- http://localhost:8000/docs
- http://localhost:8000/redoc

## Development

### Project Structure

- `app/main.py`: Main FastAPI application
- `app/models/`: Pydantic models for request/response validation
- `app/routers/`: API route handlers
- `app/services/`: Business logic
- `app/utils/`: Utility functions 