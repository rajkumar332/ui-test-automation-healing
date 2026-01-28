import requests
from services.llm_providers.base_provider import BaseLLMProvider

class OllamaProvider(BaseLLMProvider):

    def generate(self, prompt: str) -> str:
        payload = {
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
        response = requests.post("http://ollama:11434/api/generate", json=payload)
        return response.json().get("response", "")
