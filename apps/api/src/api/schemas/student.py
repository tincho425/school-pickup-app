from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class StudentBase(BaseModel):
    """Shared student fields."""

    name: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., max_length=100)
    phone_number: Optional[str] = Field(default=None, max_length=20)


class StudentCreate(StudentBase):
    """Payload for creating a student."""
    school_id: int = Field(..., gt=0, description="The ID of the school the student belongs to.")


class StudentUpdate(BaseModel):
    """Payload for updating a student."""

    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    email: Optional[str] = Field(default=None, max_length=100)
    phone_number: Optional[str] = Field(default=None, max_length=20)
    school_id: Optional[int] = Field(default=None, gt=0, description="The ID of the school the student belongs to.")

class StudentRead(StudentBase):
    """Student returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
    
    school_id: int


class StudentGuardianAssociationRead(BaseModel):
    """Association between a student and a guardian."""

    model_config = ConfigDict(from_attributes=True)

    student_id: int
    guardian_id: int
    can_pickup: bool