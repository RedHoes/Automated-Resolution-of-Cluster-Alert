from fastapi import APIRouter
from .slack import send_slack_message
from ..src.model.payload import payload
from ..src.model.response import Response
import openai
from ..src.model.shared_module import SharedVariables

router = APIRouter()

@router.post("/chatgpt")
def chatGPTCall(message: str):
    
    request_payload = payload.request_payload(message)
    
    completion = openai.ChatCompletion.create(**request_payload, headers=payload.headers) # openai.openai_object.OpenAIObject
    
    message = payload.convertToJson(completion)
    
    response = message["content"]
    
    send_slack_message(response, SharedVariables.rulename, SharedVariables.reason)
    
    return Response.chatgpt(message)