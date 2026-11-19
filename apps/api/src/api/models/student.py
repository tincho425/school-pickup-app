from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import UTC, datetime
from .base import Base

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    school = relationship("School", back_populates="students")
    school_id: Mapped[int] = mapped_column(ForeignKey("schools.id"), nullable=False, index=True)
    
    guardian_links: Mapped[List["StudentGuardianAssociation"]] = relationship("StudentGuardianAssociation", back_populates="student")
    
    pickup_events: Mapped[List["PickupEvent"]] = relationship("PickupEvent", back_populates="student")

    def __repr__(self) -> str:
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"
      
class StudentGuardianAssociation(Base):
    __tablename__ = "student_guardian_association"

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), primary_key=True)
    guardian_id: Mapped[int] = mapped_column(ForeignKey("guardians.id"), primary_key=True)
    can_pickup: Mapped[bool] = mapped_column(nullable=False, default=False)
    
    student: Mapped["Student"] = relationship("Student", back_populates="guardian_links")
    guardian: Mapped["Guardian"] = relationship("Guardian", back_populates="student_links")