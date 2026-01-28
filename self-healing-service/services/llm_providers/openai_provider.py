import openai
from services.llm_providers.base_provider import BaseLLMProvider

class OpenAIProvider(BaseLLMProvider):

    def generate(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response["choices"][0]["message"]["content"]
