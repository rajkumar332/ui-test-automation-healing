import os

import google.generativeai as genai
from services.llm_providers.base_provider import BaseLLMProvider

class GeminiProvider(BaseLLMProvider):

    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    def generate(self, prompt: str) -> str:
        model = genai.GenerativeModel("gemini-3-flash-preview")
        response = model.generate_content(prompt)
        return response.text
