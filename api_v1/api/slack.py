from fastapi import APIRouter
import requests
from ..src.model.payload import payload
from ..src.model.enum import enum
import os

router = APIRouter()

@router.post("/slack")
def send_slack_message(message: str, rulename: str, reason: str):
    try:
        payloads = payload.parse_payload(message, rulename, reason)
        webhook_url= os.getenv("WebhookURL")
        
        response = requests.post(webhook_url, json=payloads)
        
        if response.status_code == 200:
            return {"message": f"{enum.payload_send_to_slack_successfully}"}
        else:
            return {"message": f"{enum.payload_send_to_slack_fail} {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"message": f"{enum.payload_send_to_slack_fail} {response.status_code}"}
    