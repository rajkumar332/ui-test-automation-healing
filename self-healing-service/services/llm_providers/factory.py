import os

from services.llm_providers.openai_provider import OpenAIProvider
from services.llm_providers.gemini_provider import GeminiProvider
from services.llm_providers.ollama_provider import OllamaProvider
# from services.llm_providers.anthropic_provider import AnthropicProvider

def get_llm_provider():
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "openai":
        return OpenAIProvider()

    if provider == "gemini":
        return GeminiProvider()

    if provider == "ollama":
        return OllamaProvider()

    # if provider == "anthropic":
    #     return AnthropicProvider()

    raise ValueError(f"Unknown LLM provider: {provider}")
