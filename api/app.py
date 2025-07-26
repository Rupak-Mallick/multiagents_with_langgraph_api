from fastapi import FastAPI, Request
from pydantic import BaseModel
from agents.research_agent import get_research_agent
from agents.math_agent import get_math_agent
from supervisor.supervisor_agent import get_supervisor
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GROQ_API_KEY or not TAVILY_API_KEY:
    raise EnvironmentError("Please set GROQ_API_KEY and TAVILY_API_KEY in .env")

llm = init_chat_model(groq_api_key=GROQ_API_KEY, model="qwen/qwen3-32b", model_provider="groq")
research_agent = get_research_agent(llm, TAVILY_API_KEY)
math_agent = get_math_agent(llm)
supervisor = get_supervisor(llm, research_agent, math_agent)

app = FastAPI()

class UserInput(BaseModel):
    message: str

@app.post("/multiagent/run")
async def run_multiagent(user_input: UserInput):
    final_chunk = None
    stream = supervisor.stream({"messages": [{"role": "user", "content": user_input.message}]})
    for chunk in stream:
        final_chunk = chunk
    return {
        "response": final_chunk["supervisor"]["messages"][-1].content
    }