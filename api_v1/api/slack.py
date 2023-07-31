from fastapi import APIRouter
import requests
from ..src.model.payload import payload
from ..src.model.enum import SlackMessages
import os

router = APIRouter()

class Slack:
    @router.post("/slack")
    def send_slack_message(message: str, rulename: str, reason: str, status: str, alertname: str, description: str, appName: str, messages: str, language: str):
        try:
            if rulename != "None":
                payloads = payload.parse_payload_kibana(message, rulename, reason)
            if status != "None":
                payloads = payload.parse_payload_prometheus(message, status, alertname, description)
            if appName != "None":
                payloads = payload.parse_payload_log(message, appName, language, messages)
            webhook_url= os.getenv("WebhookURL")
            
            response = requests.post(webhook_url, json=payloads)
            
            if response.status_code == 200:
                return {"message": f"{SlackMessages.PAYLOAD_SEND_SUCCESS}"}
            else:
                return {"message": f"{SlackMessages.PAYLOAD_SEND_FAIL} {response.status_code}"}
        except requests.exceptions.RequestException as e:
            return {"message": f"{SlackMessages.PAYLOAD_SEND_FAIL} {response.status_code}"}
    