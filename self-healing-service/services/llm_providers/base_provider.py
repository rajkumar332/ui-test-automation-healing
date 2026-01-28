class BaseLLMProvider:

    def generate(self, prompt: str) -> str:
        raise NotImplementedError("generate() must be implemented")
