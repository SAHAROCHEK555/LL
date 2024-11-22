import requests

class MistralWork:
    @staticmethod
    def answer_from_mistral(API_KEY, message):
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        
        data = {
            "model": "mistral-small-latest",  # Specify the model you want to use
            "messages": [{"role": "user", "content": message}]
        }
        
        response = requests.post('https://api.mistral.ai/v1/chat/completions', headers=headers, json=data)
        
        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            return reply
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")