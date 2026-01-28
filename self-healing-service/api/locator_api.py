from fastapi import APIRouter
from schemas.request_schema import LocatorRequest
from schemas.response_schema import HealedLocatorResponse
from services.locator_llm_healer import LocatorLLMHealer

router = APIRouter()
healer = LocatorLLMHealer()

@router.post("/heal", response_model=HealedLocatorResponse)
def heal(request: LocatorRequest):
    result = healer.get_healed_locator(request)
    return HealedLocatorResponse(
        healed_locator=result["locator"],
        confidence=result["confidence"],
        reason=result["reason"]
    )
