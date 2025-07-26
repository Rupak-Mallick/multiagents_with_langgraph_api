# Multi-Agent FastAPI System with LangGraph

This is a FastAPI app that uses a LangGraph-powered Supervisor to coordinate:

- 🔍 Research Agent (Tavily Search)
- ➕ Math Agent (basic arithmetic)

## Setup

1. Clone repo and create `.env` file:

```bash
cp .env
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:

```bash
uvicorn api.app:app --reload
```

4. Test endpoint at:

```
POST http://localhost:8000/multiagent/run

Body:
{
  "message": "find US and New York state GDP in 2024. what % of US GDP was New York state?"
}
```

## Docker Usage

```bash
docker build -t multiagent-app .
docker run -p 8000:8000 --env-file .env multiagent-app
```
