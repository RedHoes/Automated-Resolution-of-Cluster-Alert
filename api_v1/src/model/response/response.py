from ..payload import payload
import openai
class Response():
    def chatgpt(message):
        return {"message": message}
    def handle_response(message: str):
        request_payload = payload.request_payload_prometheus(message)
        
        header = payload.getHeader()
        
        completion = openai.ChatCompletion.create(**request_payload, headers=header)
        
        message = payload.convertToJson(completion)
        
        response = message["content"]
        
        return response