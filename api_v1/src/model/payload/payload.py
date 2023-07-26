import json
import os
import openai

class payload():
    
    headers = {
        "Authorization": f"Bearer {openai.api_key}",
        "Content-Type": "application/json",
    }
    
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY") 
           
    def parse_payload(message: str, rulename: str, reason: str):
        payload = {
            "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Hey there :wave: I'm `trainee-alerts`. I'm here to help you resolve your problem.\nThere are five steps to resolve the below issue:"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":warning:  *ALERT: {rulename}*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":question:  *Reason: {reason}*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":point_right:  *SOLUTION* \n{message}"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "*This is developed by devops-trainees*"
                    },
                    {
                        "type": "image",
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
        mess = completion.choices[0].message # class 'openai.openai_object.OpenAIObject 
        openai_dict = mess.to_dict() # dict
        json_string = json.dumps(openai_dict) # str
        res = json.loads(json_string) #dict
        return res 
    
    @staticmethod
    def request_payload(message):
        request_payload = { # dict
            "messages": [
                {"role": "system", "content": "Resolve with concise 5 steps for DevOps with each step having the same length"},
                 {"role": "user", "content": f"Give me some solution to resolve this issue: {message} ?"}
            ],
            "model": "gpt-3.5-turbo",
        }
        return request_payload
