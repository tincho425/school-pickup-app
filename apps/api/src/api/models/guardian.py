from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import datetime, UTC
from .base import Base

class Guardian(Base):
    __tablename__ = "guardians"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    # Relationships
    student_links: Mapped[List["StudentGuardianAssociation"]] = relationship("StudentGuardianAssociation", back_populates="guardian")
    
    pickup_events: Mapped[List["PickupEvent"]] = relationship("PickupEvent", back_populates="guardian")