from datetime import datetime, UTC
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class PickupEvent(Base):
    __tablename__ = "pickup_events"

    id: Mapped[int] = mapped_column(primary_key=True)
    pickup_time: Mapped[datetime] = mapped_column(nullable=False)
    pickup_location: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    guardian_id: Mapped[int] = mapped_column(ForeignKey("guardians.id"), nullable=False, index=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False, index=True)
    
    student: Mapped["Student"] = relationship("Student", back_populates="pickup_events")
    guardian: Mapped["Guardian"] = relationship("Guardian", back_populates="pickup_events")
    