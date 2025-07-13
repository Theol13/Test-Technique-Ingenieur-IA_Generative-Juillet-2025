from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.openrouter_service import ask_openrouter

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask")
def ask(prompt_request: PromptRequest):
    result = ask_openrouter(prompt_request.prompt)
    return {"response": result}
