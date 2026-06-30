# Student Library

Ein kleines Python-Projekt zum Üben von Unit-Tests.

Ein Student kann nur dann einen Bibliotheksausweis beantragen, wenn die Studiengebühr bezahlt wurde. In diesem Projekt bedeutet "bezahlt" also "immatrikuliert".

## Was enthalten ist

- eine kleine In-Memory-Datenbank für Studierende
- ein Service, der entscheidet, ob ein Bibliotheksausweis ausgestellt werden darf
- Unit-Tests mit dem eingebauten Modul `unittest`

## Tests ausführen

```bash
python -m unittest discover -s tests
```
