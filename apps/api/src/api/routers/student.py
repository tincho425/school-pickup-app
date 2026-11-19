from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies import get_session
from api.models.student import Student
from api.schemas.student import StudentCreate, StudentRead, StudentUpdate


router = APIRouter(prefix="/students", tags=["students"])


@router.get("/", response_model=list[StudentRead])
async def list_students(session: AsyncSession = Depends(get_session)) -> list[Student]:
	result = await session.execute(select(Student))
	return list(result.scalars().all())


@router.get("/{id}", response_model=StudentRead)
async def get_student(id: int, session: AsyncSession = Depends(get_session)) -> Student:
	student = await session.get(Student, id)
	if student is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
	return student


@router.post("/", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
async def create_student(
	student_data: StudentCreate,
	session: AsyncSession = Depends(get_session),
) -> Student:
	student = Student(**student_data.model_dump())
	session.add(student)
	await session.commit()
	await session.refresh(student)
	return student


@router.patch("/{id}", response_model=StudentRead)
async def update_student(
	id: int,
	student_data: StudentUpdate,
	session: AsyncSession = Depends(get_session),
) -> Student:
	student = await session.get(Student, id)
	if student is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

	for field, value in student_data.model_dump(exclude_unset=True).items():
		setattr(student, field, value)

	await session.commit()
	await session.refresh(student)
	return student


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(id: int, session: AsyncSession = Depends(get_session)) -> Response:
	student = await session.get(Student, id)
	if student is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

	await session.delete(student)
	await session.commit()
	return Response(status_code=status.HTTP_204_NO_CONTENT)
