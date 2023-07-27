from fastapi import APIRouter
import json
from ..api.chatgpt import chatGPT
from ..src.model.kibana import kibana_alert
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
        return kibana_alert.alert(message) 
    @router.post("/prometheus/alert")
    async def receive_alert(request: Request):
        body = await request.body()
        data = json.loads(body.decode())
        print(data)
        return data
