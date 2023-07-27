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
        message = f"Message: {SharedVariables.reason}"
        chatGPT.chatGPTCall(message)  
        return Input.kibana_alert(message) 
    @router.post("/prometheus/alert")
    async def receive_alert(request: Request):
        body = await request.body()
        data = json.loads(body.decode())
        SharedVariables.alertname = data["commonLabels"]["alertname"]
        SharedVariables.status = data["status"]
        SharedVariables.description = data["alerts"][0]["annotations"]["description"]
        if data.get("status") == "firing":
            message = f"Message: {SharedVariables.description}"
            chatGPT.chatGPTCall(message)  
        return Input.prometheus_alert(message)
    @router.post("prometheus/logs")
    async def receive_logs(request: Request):
        body = await request.body()
        data = json.loads(body.decode())
        print(data)
        message = f"Message: {data}"
        # Manage message
        # call to chatGPT
        return Input.prometheus_log(message)
    