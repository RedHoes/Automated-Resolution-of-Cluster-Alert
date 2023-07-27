from fastapi import APIRouter
from .slack import Slack
from ..src.model.payload import payload
from ..src.model.response import Response
import openai
from ..src.model.shared_module import SharedVariables

router = APIRouter()

class chatGPT:
    @router.post("/chatgpt")
    def chatGPTCall(message: str):
        
        request_payload = payload.request_payload(message)
        
        header = payload.getHeader()
        
        completion = openai.ChatCompletion.create(**request_payload, headers=header)
        
        message = payload.convertToJson(completion)
        
        response = message["content"]
        
        Slack.send_slack_message(response, SharedVariables.rulename, SharedVariables.reason, SharedVariables.status, SharedVariables.alertname, SharedVariables.description)
        
        return Response.chatgpt(message)
    