from ..payload import payload
import openai
class Response():
    def chatgpt(message):
        return {"message": message}
    def handle_response_kibana(message: str):
        request_payload = payload.request_payload_kibana(message)
        
        header = payload.getHeader()
        
        completion = openai.ChatCompletion.create(**request_payload, headers=header)
        
        message = payload.convertToJson(completion)
        
        response = message["content"]
        
        return response
    def handle_response_prometheus(message: str):
        request_payload = payload.request_payload_prometheus(message)
        
        header = payload.getHeader()
        
        completion = openai.ChatCompletion.create(**request_payload, headers=header)
        
        message = payload.convertToJson(completion)
        
        response = message["content"]
        
        return response
    def handle_response_log(message: str):
        request_payload = payload.request_payload_log(message)
        
        header = payload.getHeader()
        
        completion = openai.ChatCompletion.create(**request_payload, headers=header)
        
        message = payload.convertToJson(completion)
        
        response = message["content"]
        
        return response