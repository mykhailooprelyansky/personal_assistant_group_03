from collections import UserDict, UserList


class Note:
    def __init__(self, text):
        self.text = text
        self.tags = []

    def __str__(self):
        return f"This note: {self.text}, has tags: {'; '.join(p for p in self.tags)}"

    def add_tag(self, tag):
        if tag.isspace():
            raise ValueError("Tag may be one long word without space")
        self.tags.append(tag)


class Notes(UserList):
    def __init__(self):
        self.data = []
        self.counter = -1

    def add(self, note: Note):
        note_info = {'text': note.text,
                   'tags': note.tags}
        self.data.append(note_info)
        print(f"Yours note has been added to NoteBook.")

    def find(self, tag):
        for notes in self.data:
            for tag_list in notes['tags']:
                if tag in tag_list:
                    return notes
        


notebook = Notes()

note1 = Note("This is my first note in this notebook")

note1.add_tag("r1234567890")
note1.add_tag("77777")
note1.add_tag("gfg")
print(note1) 
notebook.add(note1)


note2 = Note("This note is about weather")
note2.add_tag("weather")
print(note2)
notebook.add(note2)


note_weather = notebook.find("weather")
print(note_weather['text'])
print(note_weather['tags'])
