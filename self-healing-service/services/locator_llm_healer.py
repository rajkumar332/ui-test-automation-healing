import logging
import os

from services.llm_providers.factory import get_llm_provider
from services.signature_store import SignatureStore
from utils.prompt_builder import build_prompt


class LocatorLLMHealer:

    def __init__(self):
        self.store = SignatureStore()
        self.llm = get_llm_provider()

    def get_healed_locator(self, req):

        saved = self.store.get(req.element_key)
        print(saved)
        if not saved:
            return {
                "locator": req.failed_locator,
                "confidence": 1.0,
                "reason": "No signature stored yet."
            }

        prompt = build_prompt(
            req.failed_locator,
            saved["old_dom"],
            req.new_dom,
            saved["signature"],
            saved["neighbors"],
            saved["intent"]
        )

        llm_response = self.llm.generate(prompt)

        try:
            result = eval(llm_response)
        except:
            result = {"locator": req.failed_locator, "confidence": 0.0}
            logging.log(logging.ERROR, f"LLM response parsing failed: {llm_response}")

        return {
            "locator": result["locator"],
            "confidence": result["confidence"],
            "reason": f"Successfully healed"
        }
