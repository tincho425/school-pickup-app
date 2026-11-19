from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class GuardianBase(BaseModel):
    name: str
    email: str
    phone_number: Optional[str] = None
    
class GuardianCreate(GuardianBase):
    """Payload for creating a guardian."""

class GuardianUpdate(BaseModel):
    """Payload for updating a guardian."""

    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    
class GuardianRead(GuardianBase):
    """Guardian returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime