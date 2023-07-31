from fastapi import APIRouter, HTTPException
import json
from ..api.chatgpt import chatGPT
from ..src.model.input import Input
from fastapi import Request
from ..src.model.shared_module import SharedVariables

router = APIRouter()

class alert:
    @router.post("/kibana/alert")
    async def receive_webhook(request: Request):
        try:
            body = await request.body()
            data = json.loads(body.decode())
            
            SharedVariables.rulename = data["rulename"]
            SharedVariables.reason = data["reason"]
            SharedVariables.define_value_kibana()
            
            message = f"Message: {SharedVariables.reason}"
            chatGPT.chatGPTCallkibana(message)  
            
            return Input.kibana_alert(message) 
        except KeyError as e:
            raise HTTPException(status_code=400, detail=f"Missing required key: {e}")
        except json.JSONDecodeError as e:
            raise HTTPException(status_code=400, detail="Invalid JSON data")
    
    @router.post("/prometheus/alert")
    async def receive_alert(request: Request):
        try: 
            body = await request.body()
            data = json.loads(body.decode())
            
            SharedVariables.alertname = data["commonLabels"]["alertname"]
            SharedVariables.status = data["status"]
            SharedVariables.description = data["alerts"][0]["annotations"]["description"]
            SharedVariables.define_value_prometheus()
            
            if data.get("status") == "firing":
                message = f"Message: {SharedVariables.description}"
                chatGPT.chatGPTCallprometheus(message)  
                
            return Input.prometheus_alert(message)
        except KeyError as e:
            raise HTTPException(status_code=400, detail=f"Missing required key: {e}")
        except json.JSONDecodeError as e:
            raise HTTPException(status_code=400, detail="Invalid JSON data")
    
    @router.post("/app/logs")
    async def receive_logs(request: Request):
        try:
            body = await request.body()
            data = json.loads(body.decode())
            
            SharedVariables.appName = data["appName"]
            SharedVariables.language = data["language"]
            SharedVariables.message = data["message"]
            SharedVariables.define_value_log()
            
            message = f"Message: {SharedVariables.message}"
            chatGPT.chatGPTCalllog(message)  
            
            return Input.App_log(message)
        except KeyError as e:
            raise HTTPException(status_code=400, detail=f"Missing required key: {e}")
        except json.JSONDecodeError as e:
            raise HTTPException(status_code=400, detail="Invalid JSON data")
