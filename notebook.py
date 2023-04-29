from collections import UserDict
import argparse
import datetime


class _HashTag:
    def __init__(self, tag):
        self.tag = tag

    def __str__(self):
        return f"{self.tag}"


class _Note:
    def __init__(self, note_title: str, note, tags: list[_HashTag] = None):
        self.note_title = note_title
        self.note = note
        self.tags = tags

    def __str__(self):
        res = ["_" * 100
               + "\n"f"Note '{self.note_title}':\n\n{self.note}\n{''.join(f'#{tag}' for tag in self.tags)}\n"
               + "_" * 100
               + "\n"]
        return "\n".join(res)


class NoteBook(UserDict):
    def add_note(self, note: _Note):
        if note.note_title in self.data.keys():
            return "Notebook already contain the note with the same title."
        else:
            self.data[note.note_title] = note

    def __str__(self):
        return "\n".join(str(n) for n in self.data.values())


notebook = NoteBook()


def create_note(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument("note_title", nargs="?", help="Note Title")
    parser.add_argument("note_text", nargs="*", help="Text of the note")
    parser.add_argument("-t", "--tags", nargs="*", help="Tags for note")
    args = parser.parse_args(args)
    note_title = args.note_title
    if note_title in notebook.keys():
        note_title += f" {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    tags = [_HashTag(tag) for tag in args.tags] if args.tags else []
    note = _Note(note_title, " ".join(args.note_text), tags)
    notebook.add_note(note)


def show(*args):
    for note in notebook.values():
        print(note)
    return ""


COMMANDS = {create_note: "create", show: "show"}


def command_handler(user_input: str):
    for command, command_words in COMMANDS.items():
        if user_input.lower().startswith(command_words):
            return command, user_input[len(command_words):].strip().split(" ")
    return None, None


def main():
    while True:
        user_input = input("Enter command:\n")
        command, data = command_handler(user_input)
        print(data)
        if command:
            print(command(*data))
        elif any(
            word in user_input.lower()
            for word in ["exit", "close", "good bye", "goodbye"]
        ):
            print("Good bye!")
            break


if __name__ == "__main__":
    main()
