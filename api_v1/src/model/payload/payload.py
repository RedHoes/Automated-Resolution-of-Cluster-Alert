import json
import os
import openai
from ..enum import MessageTypes

class payload:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY") 
           
    def getHeader():
        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "Content-Type": "application/json",
        }       
        return headers       
           
    def parse_payload_kibana(message: str, rulename: str, reason: str):
        payload = {
            "blocks": [
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": "Hey there :wave: I'm `trainee-alerts`. I'm here to help you resolve your problem.\nThere are five steps to resolve the below issue:"
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":warning:  *ALERT NAME: {rulename}*"
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":question:  *Reason: {reason}*"
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":point_right:  *SOLUTION* \n{message}"
                }
            },
            {
                "type": MessageTypes.CONTEXT,
                "elements": [
                    {
                        "type": MessageTypes.MRKDWN,
                        "text": "*This is developed by devops-trainees*"
                    },
                    {
                        "type": MessageTypes.IMAGE,
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTRjjlDvUCrIh10Bjm5FyMq0GaM4v9riT2U3wriY9gVcm3b0sw4jq5U9dySnkTuQtepJo&usqp=CAU",
                        "alt_text": "nfq_logo"
                    }
                ]
            }
            ]
        }
        return payload
    
    def parse_payload_prometheus(message: str, status: str, alertname: str, description: str):
        payload = {
            "blocks": [
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": "Hey there :wave: I'm `trainee-alerts`. I'm here to help you resolve your problem.\nThere are five steps to resolve the below issue:"
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":warning:  *ALERT NAME: {alertname}*"
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":question:  *Status: {status}*"
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":alert:  *Status: {description}*"
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":point_right:  *SOLUTION* \n{message}"
                }
            },
            {
                "type": MessageTypes.CONTEXT,
                "elements": [
                    {
                        "type": MessageTypes.MRKDWN,
                        "text": "*This is developed by devops-trainees*"
                    },
                    {
                        "type": MessageTypes.IMAGE,
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTRjjlDvUCrIh10Bjm5FyMq0GaM4v9riT2U3wriY9gVcm3b0sw4jq5U9dySnkTuQtepJo&usqp=CAU",
                        "alt_text": "nfq_logo"
                    }
                ]
            }
            ]
        }
        return payload

    @staticmethod
    def convertToJson(completion):
        mess = completion.choices[0].message
        openai_dict = mess.to_dict()
        json_string = json.dumps(openai_dict) 
        res = json.loads(json_string)
        return res 
    
    @staticmethod
    def request_payload_kibana(message):
        new_message = payload.parse_message(message)
        request_payload = { 
            "messages": [
                {"role": "system", "content": "Resolve with concise 5 steps for DevOps with each step having the same length"},
                {"role": "user", "content": f"my kibana alert return this message: {new_message}, help me to resolve it"}
            ],
            "model": "gpt-3.5-turbo",
        }
        return request_payload
    
    @staticmethod
    def request_payload_prometheus(message):
        new_message = payload.parse_message(message)
        request_payload = { 
            "messages": [
                {"role": "system", "content": "Resolve with concise 5 steps for DevOps with each step having the same length"},
                {"role": "user", "content": f"my alert manager from prometheus return this message: {new_message}, help me to resolve it"}
            ],
            "model": "gpt-3.5-turbo",
        }
        return request_payload
    
    @staticmethod
    def parse_message(message: str):
        sentences = message.split('.')
        sentence = sentences[0].strip()
        return sentence

