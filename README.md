# The Mom Test Bot

A web application that helps entrepreneurs validate their startup ideas using principles from "The Mom Test" by Rob Fitzpatrick.

## What is The Mom Test?

The Mom Test is a set of principles for customer conversations that help entrepreneurs get honest feedback about their ideas. The core principle is to talk about the customer's life, not your idea, and to ask about specifics in the past rather than generics or opinions about the future.

## Features

- Generate interview questions based on The Mom Test principles
- Create validation plans for startup ideas
- Record and analyze customer interview results
- Get AI-powered insights on your validation progress

## Tech Stack

This is a monorepo built with:

- **Frontend**: Next.js, React, TailwindCSS
- **Backend**: FastAPI, Python
- **Package Manager**: pnpm
- **Monorepo Tools**: Turborepo
- **UI Library**: Custom components with shadcn/ui principles
- **Database**: Supabase
- **Authentication**: Supabase Auth
- **AI**: OpenAI API

## Project Structure

```
themomtestbot/
├── apps/
│   ├── web/           # Next.js frontend
│   └── api/           # FastAPI backend
├── packages/
│   └── ui/            # Shared UI components
└── turbo.json         # Turborepo configuration
```

## Getting Started

### Prerequisites

- Node.js 18+
- pnpm 8+
- Python 3.11+

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/themomtestbot.git
   cd themomtestbot
   ```

2. Install dependencies:
   ```
   pnpm install
   ```

3. Set up environment variables:
   ```
   cp apps/web/.env.example apps/web/.env.local
   cp apps/api/.env.example apps/api/.env
   ```

4. Start the development servers:
   ```
   pnpm dev
   ```

## Development

### Frontend (Next.js)

The frontend is located in `apps/web`. To run it separately:

```
pnpm --filter web dev
```

### Backend (FastAPI)

The backend is located in `apps/api`. To run it separately:

```
cd apps/api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### UI Components

Shared UI components are located in `packages/ui`. To build them:

```
pnpm --filter ui build
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Rob Fitzpatrick for writing "The Mom Test"
- The Turborepo team for the monorepo tooling