from services.notes_loader import NotesLoader

print("=" * 50)
print("TrippyPrep Notes Loader")
print("=" * 50)

notes = NotesLoader.load(
    "notes/aptitude/01_foundation/number_system.md"
)

print(notes)