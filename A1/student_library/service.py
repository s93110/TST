from __future__ import annotations

from .models import LibraryCard
from .repository import InMemoryStudentDatabase


class EnrollmentError(ValueError):
    pass


class LibraryCardService:
    def __init__(self, database: InMemoryStudentDatabase) -> None:
        self._database = database

    def request_card(self, student_id: str) -> LibraryCard:
        student = self._database.get_student(student_id)
        if not student.tuition_paid:
            raise EnrollmentError("Ein Student muss die Studiengebühr bezahlt haben, bevor er einen Bibliotheksausweis beantragen kann.")

        return LibraryCard(card_id=f"LIB-{student.student_id}", student_id=student.student_id)
