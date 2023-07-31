from fastapi import APIRouter
from .slack import Slack
from ..src.model.payload import payload
from ..src.model.response import Response
from ..src.model.shared_module import SharedVariables

router = APIRouter()

class chatGPT:
    @router.post("/chatgpt/kibana")
    def chatGPTCallkibana(message: str):
        
        response = Response.handle_response_kibana(message)
        
        Slack.send_slack_message(response, SharedVariables.rulename, SharedVariables.reason, SharedVariables.status, SharedVariables.alertname, SharedVariables.description, SharedVariables.appName, SharedVariables.message, SharedVariables.language)
        
        return Response.chatgpt(message)
    
    @router.post("/chatgpt/prometheus")
    def chatGPTCallprometheus(message: str):
        
        response = Response.handle_response_prometheus(message)
        
        Slack.send_slack_message(response, SharedVariables.rulename, SharedVariables.reason, SharedVariables.status, SharedVariables.alertname, SharedVariables.description, SharedVariables.appName, SharedVariables.message, SharedVariables.language)
        
        return Response.chatgpt(message)
    
    @router.post("/chatgpt/APM")
    def chatGPTCalllog(message: str):
        
        response = Response.handle_response_log(message)
        
        Slack.send_slack_message(response, SharedVariables.rulename, SharedVariables.reason, SharedVariables.status, SharedVariables.alertname, SharedVariables.description, SharedVariables.appName, SharedVariables.message, SharedVariables.language)
        
        return Response.chatgpt(message)
