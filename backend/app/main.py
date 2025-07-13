from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.openrouter_service import ask_openrouter
from app.local_model_service import ask_local_model

app = FastAPI()

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