import json
import os
import openai
from ..enum import enum

class payload:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY") 
           
    def getHeader():
        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "Content-Type": "application/json",
        }       
        return headers       
           
    def parse_payload(message: str, rulename: str, reason: str):
        payload = {
            "blocks": [
            {
                "type": enum.SECTION,
                "text": {
                    "type": enum.MRKDWN,
                    "text": "Hey there :wave: I'm `trainee-alerts`. I'm here to help you resolve your problem.\nThere are five steps to resolve the below issue:"
                }
            },
            {
                "type": enum.SECTION,
                "text": {
                    "type": enum.MRKDWN,
                    "text": f":warning:  *ALERT: {rulename}*"
                }
            },
            {
                "type": enum.SECTION,
                "text": {
                    "type": enum.MRKDWN,
                    "text": f":question:  *Reason: {reason}*"
                }
            },
            {
                "type": enum.SECTION,
                "text": {
                    "type": enum.MRKDWN,
                    "text": f":point_right:  *SOLUTION* \n{message}"
                }
            },
            {
                "type": enum.CONTEXT,
                "elements": [
                    {
                        "type": enum.MRKDWN,
                        "text": "*This is developed by devops-trainees*"
                    },
                    {
                        "type": enum.IMAGE,
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
    def request_payload(message):
        request_payload = { 
            "messages": [
                {"role": "system", "content": "Resolve with concise 5 steps for DevOps with each step having the same length"},
                 {"role": "user", "content": f"Give me some solution to resolve this issue: {message} ?"}
            ],
            "model": "gpt-3.5-turbo",
        }
        return request_payload
