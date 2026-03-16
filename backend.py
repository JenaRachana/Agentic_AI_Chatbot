#step-1 : Setup Pydantic Model (Schema Validation)

from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool



#step-2 : Setup AI Agent from FrontEnd Request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent
import uvicorn

app=FastAPI(title='LanGgraph Ai Agent')

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the Chatbot using LanGgraph and search tools.
    It dynamically sealects the model specified in the request
    """
    llm_id = request.model_name
    query = " ".join(request.messages)
    allow_search = request.allow_search
    provider = request.model_provider
    system_prompt = request.system_prompt

    response =get_response_from_ai_agent(llm_id,query,allow_search,provider,system_prompt)
    return response

#step-3 : Run app & Explore Swagger UI Docs

if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)

