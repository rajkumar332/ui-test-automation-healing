from pydantic import BaseModel

class HealedLocatorResponse(BaseModel):
    healed_locator: str
    confidence: float
    reason: str
