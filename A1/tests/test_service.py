from pathlib import Path
import sys
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from student_library import service
from student_library import EnrollmentError, InMemoryStudentDatabase, LibraryCardService, Student


class LibraryCardServiceTests(unittest.TestCase):
    def test_ausweis_fuer_bezahlten_studenten_wird_ausgestellt(self) -> None:
        database = InMemoryStudentDatabase()
        database.add_student(Student(student_id="S-100", name="Mila", tuition_paid=True))
        service = LibraryCardService(database)

        card = service.request_card("S-100")

        self.assertEqual(card.card_id, "LIB-S-100")
        self.assertEqual(card.student_id, "S-100")

    def test_ausweis_wird_fuer_unbezahlten_studenten_abgelehnt(self) -> None:
        database = InMemoryStudentDatabase()
        database.add_student(Student(student_id="S-200", name="Noah", tuition_paid=False))
        service = LibraryCardService(database)

        with self.assertRaisesRegex(EnrollmentError, "Studiengebühr bezahlt haben"):
            service.request_card("S-200")

    def test_bezahlung_setzt_immatrikulation_auf_wahr(self) -> None:
        database = InMemoryStudentDatabase()
        database.add_student(Student(student_id="S-300", name="Lea"))

        self.assertFalse(database.has_paid("S-300"))

        database.mark_tuition_paid("S-300")

        self.assertTrue(database.has_paid("S-300"))

    def test_exeption_for_non_existing_student(self) -> None:
        database = InMemoryStudentDatabase()

        self.assertRaisesRegex(KeyError, "Unbekannte student_id: S-400", database.get_student, "S-400")


if __name__ == "__main__":
    unittest.main()
