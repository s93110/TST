from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Student:
    student_id: str
    name: str
    tuition_paid: bool = False


@dataclass(frozen=True, slots=True)
class LibraryCard:
    card_id: str
    student_id: str
