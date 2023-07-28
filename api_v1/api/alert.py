from fastapi import APIRouter
import json
from ..api.chatgpt import chatGPT
from ..src.model.input import Input
from fastapi import Request
from ..src.model.shared_module import SharedVariables

router = APIRouter()

class alert:
    @router.post("/kibana/alert")
    async def receive_webhook(request: Request):
        body = await request.body()
        data = json.loads(body.decode())
        SharedVariables.rulename = data["rulename"]
        SharedVariables.reason = data["reason"]
        SharedVariables.alertname = "None"
        SharedVariables.status = "None"
        SharedVariables.description = "None"
        SharedVariables.appName = "None"
        SharedVariables.language = "None"
        SharedVariables.message = "None"
        message = f"Message: {SharedVariables.reason}"
        chatGPT.chatGPTCallkibana(message)  
        return Input.kibana_alert(message) 
    
    @router.post("/prometheus/alert")
    async def receive_alert(request: Request):
        # try catch
        body = await request.body()
        data = json.loads(body.decode())
        SharedVariables.alertname = data["commonLabels"]["alertname"]
        SharedVariables.status = data["status"]
        SharedVariables.description = data["alerts"][0]["annotations"]["description"]
        SharedVariables.rulename = "None"
        SharedVariables.reason = "None"
        SharedVariables.appName = "None"
        SharedVariables.language = "None"
        SharedVariables.message = "None"
        if data.get("status") == "firing":
            message = f"Message: {SharedVariables.description}"
            chatGPT.chatGPTCallprometheus(message)  
        return Input.prometheus_alert(message)
    
    @router.post("/app/logs")
    async def receive_logs(request: Request):
        body = await request.body()
        data = json.loads(body.decode())
        SharedVariables.appName = data["appName"]
        SharedVariables.language = data["language"]
        SharedVariables.message = data["message"]
        SharedVariables.alertname = "None"
        SharedVariables.status = "None"
        SharedVariables.description = "None"
        SharedVariables.rulename = "None"
        SharedVariables.reason = "None"
        message = f"Message: {SharedVariables.message}"
        chatGPT.chatGPTCallAPM(message)  
        return Input.APM_log(message)
    