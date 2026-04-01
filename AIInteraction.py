import requests

class AIInteraction:
    def __init__(self, api_key=None):
        """Initialize with Ollama local model (api_key parameter kept for compatibility)"""
        self.base_url = 'http://localhost:11434/api'
        self.model = 'gemma3'

    def ask_openai(self, question):
        """Ask the Ollama gemma3 model a question"""
        try:
            payload = {
                'model': self.model,
                'messages': [
                    {'role': 'system', 'content': 'You are a helpful assistant.'},
                    {'role': 'user', 'content': question}
                ],
                'stream': False
            }
            response = requests.post(
                f'{self.base_url}/chat',
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            return result['message']['content']
        except Exception as e:
            print(f"Error with Ollama API: {e}")
            return "Sorry, I couldn't fetch an answer at the moment."