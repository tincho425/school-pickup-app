from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class PickupEventBase(BaseModel):
    pickup_time: datetime
    pickup_location: str
    
    guardian_id: int
    student_id: int
    
class PickupEventCreate(PickupEventBase):
    """Payload for creating a pickup event."""
    
class PickupEventUpdate(BaseModel):
    """Payload for updating a pickup event."""

    pickup_time: Optional[datetime] = None
    pickup_location: Optional[str] = None
    
    guardian_id: Optional[int] = None
    student_id: Optional[int] = None
    
class PickupEventRead(PickupEventBase):
    """Pickup event returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime  