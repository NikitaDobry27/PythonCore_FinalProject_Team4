import re
import datetime
from collections import UserDict


class _HashTag:
    def __init__(self, tag):
        self.tag = tag

    def __str__(self):
        return f"{self.tag}"


class _Note:
    def __init__(self, note_title: str, note_text: str, tags: list[_HashTag] = None):
        self.note_title = note_title
        self.note_text = note_text
        self.tags = tags

    def set_new_tag(self, tag: _HashTag | list[_HashTag]):
        self.tags.extend(tag) if type(tag) == list else self.tags.append(tag)

    def __str__(self):
        tags_str = "#" + " #".join(str(tag) for tag in self.tags)
        res = ["_" * 100
               + f"\nNote '{self.note_title}':\n\n{self.note_text}\n{tags_str}\n"
               + "_" * 100
               + "\n"]
        return "\n".join(res)


class NoteBook(UserDict):

    def create_note(self):
        note_title = input("Enter note title: ")
        # Если заметка с таким же заголовком уже существует, то к названию плюсуеться текущее дата и время
        if note_title in notebook.keys():
            note_title += f" {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        note_content = input("Enter note text: ")
        tags_str = input("Enter tags (space separated): ").strip()
        tags_list = tags_str.split()
        tags = [_HashTag(tag.strip()) for tag in tags_list]
        new_note = _Note(note_title, note_content, tags)
        self.add_note(new_note)

        print(f"Note '{note_title}' created successfully!")
        return ""

    def add_note(self, note: _Note):
        self.data[note.note_title] = note

    def ask_note(self):
        print("Choose the note you want to work with.")
        titles = []
        for i, title in enumerate(self.data.keys(), 1):
            titles.append(title)
            print(f"{i}. {title}")
        while True:
            try:
                pos_input = input("Enter positional number of the note or 'exit':\n")
                if pos_input.lower() == "exit":
                    return "exiting..."
                title_pos = int(pos_input) - 1
                if title_pos > len(self.data.keys()) or title_pos < 0:
                    raise IndexError
            except IndexError:
                print("Wrong position. Please try again.")
                continue
            except ValueError:
                print("Please enter a valid integer index.")
                continue
            return titles[title_pos]

    def change_note(self):
        note_title = self.ask_note()
        note = self.data[note_title].note
        ch_note = input(f"Your old note:\n{note}\nYou can do a few changes by copy/paste old note, or create new one\n")
        self.data[note_title].note = ch_note
        print("DONE")
        return ""

    def del_note(self):
        note_title = self.ask_note()
        self.data.pop(note_title)
        print(f"Note '{note_title}' was successfully deleted.")
        return ""

    def show_notes(self):
        for note in self.data.values():
            print(note)
            return ""

    def search_note(self):
        query = input("Enter search query: ")
        results = []
        for note in self.data.values():
            if re.search(query, note.note_title, re.IGNORECASE) or re.search(query, note.note_text, re.IGNORECASE):
                results.append(note)
        if results:
            for note in results:
                print(f"Was found {len(results)} note(s):\n{note}")
        else:
            print("No notes found.")
        return ""

    def __str__(self):
        return "\n".join(str(n) for n in self.data.values())


notebook = NoteBook()

if __name__ == "__main__":
    notebook.create_note()
    notebook.create_note()
    notebook.show_notes()
    notebook.search_note()
