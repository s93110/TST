from __future__ import annotations

from dataclasses import replace

from .models import Student


class InMemoryStudentDatabase:
    def __init__(self) -> None:
        self._students: dict[str, Student] = {}

    def add_student(self, student: Student) -> None:
        self._students[student.student_id] = student

    def get_student(self, student_id: str) -> Student:
        try:
            return self._students[student_id]
        except KeyError as exc:
            raise KeyError(f"Unbekannte student_id: {student_id}") from exc

    def mark_tuition_paid(self, student_id: str) -> None:
        student = self.get_student(student_id)
        self._students[student_id] = replace(student, tuition_paid=True)

    def has_paid(self, student_id: str) -> bool:
        return self.get_student(student_id).tuition_paid
