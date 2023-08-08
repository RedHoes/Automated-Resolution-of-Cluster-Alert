import json
import os
import openai
from ..enum import MessageTypes
from ..shared_module import SharedVariables

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
                    "text": MessageTypes.TEXT
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
                        "text": MessageTypes.ELEMENT
                    },
                    {
                        "type": MessageTypes.IMAGE,
                        "image_url": MessageTypes.URL,
                        "alt_text": MessageTypes.LOGO
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
                    "text": MessageTypes.TEXT
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
                    "text": f":fire:  *Status: {status}*"
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":question:  *Description: {description}*"
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
                        "text": MessageTypes.ELEMENT
                    },
                    {
                        "type": MessageTypes.IMAGE,
                        "image_url": MessageTypes.URL,
                        "alt_text": MessageTypes.LOGO
                    }
                ]
            }
            ]
        }
        return payload

    def parse_payload_log(message: str, appName: str, language: str, messages: str):
        payload = {
            "blocks": [
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": MessageTypes.TEXT
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":warning:  *APP NAME: {appName}*"
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":globe_with_meridians:  *Language: {language}*"
                }
            },
            {
                "type": MessageTypes.SECTION,
                "text": {
                    "type": MessageTypes.MRKDWN,
                    "text": f":fire:  *Status: {messages}*"
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
                        "text": MessageTypes.ELEMENT
                    },
                    {
                        "type": MessageTypes.IMAGE,
                        "image_url": MessageTypes.URL,
                        "alt_text": MessageTypes.LOGO
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
                {"role": "system", "content": "Runbook to resolve this problem from kibana alert in Kubernetes"},
                {"role": "user", "content": f"{new_message}"}
            ],
            "model": "gpt-3.5-turbo",
        }
        return request_payload
    
    @staticmethod
    def request_payload_prometheus(message):
        new_message = payload.parse_message(message)
        request_payload = { 
            "messages": [
                {"role": "system", "content": "Runbook to resolve this problem for alert manager from prometheus in Kubernetes"},
                {"role": "user", "content": f"{new_message}"}
            ],
            "model": "gpt-3.5-turbo",
        }
        return request_payload
    
    @staticmethod
    def request_payload_log(message):
        new_message = payload.parse_message(message)
        language = SharedVariables.language
        request_payload = { 
            "messages": [
                {"role": "system", "content": f"Runbook to resolve this problem for {language}"},
                {"role": "user", "content": f"{new_message}"}
            ],
            "model": "gpt-3.5-turbo",
        }
        return request_payload
    
    @staticmethod
    def parse_message(message: str):
        sentences = message.split('.')
        sentence = sentences[0].strip()
        return sentence

