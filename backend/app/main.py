from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.openrouter_service import ask_openrouter
from app.local_model_service import ask_local_model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask")
def ask(prompt_request: PromptRequest):
    result = ask_openrouter(prompt_request.prompt)
    return {"response": result}

@app.post("/ask-local")
def ask_local(prompt_request: PromptRequest):
    result = ask_local_model(prompt_request.prompt)
    return {"response": result}