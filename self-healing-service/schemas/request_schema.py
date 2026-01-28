from pydantic import BaseModel

class LocatorRequest(BaseModel):
    element_key: str
    failed_locator: str
    new_dom: str       # DOM where locator failed
