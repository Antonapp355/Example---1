import modul_id
import json
import view


# Создание заметки
def add_note():
    heading = view.add_TEXT()
    text = view.add_text()
    note = {
            'ID': modul_id.iD_name(),
            'Heading': heading,
            'Note': text
            }
    with open(f"Notebook_folder/notebooks/{heading}.json", "w", encoding="utf-8") as write_file:
        write_file.write(json.dumps(note, ensure_ascii=False))
