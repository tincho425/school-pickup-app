from typing import Optional
from pydantic import BaseModel, ConfigDict

class SchoolBase(BaseModel):
    name: str
    address: str
    city: str
    state: str
    zip_code: str
    
class SchoolCreate(SchoolBase):
    """Payload for creating a school."""
    
class SchoolUpdate(BaseModel):
    """Payload for updating a school."""

    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    
class SchoolRead(SchoolBase):
    """School returned by the API."""
    
    model_config = ConfigDict(from_attributes=True)

    id: int