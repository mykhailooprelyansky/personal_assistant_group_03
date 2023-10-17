from collections import UserDict
from tkinter import messagebox
from tkinter import *

class Note:
    def __init__(self, text):
        self.text = text
        self.tags = []

    def __str__(self):
        return f"This note: {self.text}, has tags: {'; '.join(p for p in self.tags)}"

    def add_tag(self, tag):
        for ch in tag:
            if ch.isspace():
                raise ValueError("Tag may be one long word without space")
        self.tags.append(tag)

class Notes(UserDict):
    def __init__(self):
        self.data = []
        self.counter = -1

    def __iter__(self):
        return iter(self.data)
    
    def add(self, note:Note):
        note_info = {'text': note.text,
                   'tags': note.tags}
        self.data.append(note_info)
        print(f"Yours note has been added to NoteBook.")

    def find(self, find_text, find_by_tag=True):
        if find_by_tag:
            fild = 'tags'
        else:
            fild = 'text'

        for notes in self.data:
            for note in notes[fild]:
                if find_text in note:
                    return notes
    
    def delete(self, note):
        if note in self.data:
            self.data.remove(note)        
    
    def sort(self):
        pass  

    def edit_note(self, note):
        root = Tk()
        text = Text(root, width=200, height=200)
        text.pack()

        root.title = "Notes"
        root.geometry("200x200")
        def edit_text():
            text.delete('1.0', END)
            text.insert('1.0', note['text'])

        def save_text():
            note['text'] = text.get('1.0', END)
        
        def edit_tags():
            text.delete('1.0', END)
            text.insert('1.0', '\n'.join(p for p in note['tags']))
            
        def save_tags():
            edit_tags = text.get('1.0', END)
            edit_tags = edit_tags.split("\n")
            note['tags'].clear()
            flag_ok = True
            for tag in edit_tags:
                for ch in tag:
                    if ch.isspace():
                        messagebox.showerror(None, f'Tag "{tag}" consist space')
                        flag_ok = False
                        break
                
            if flag_ok:
                note['tags'].extend(edit_tags)

        main_menu = Menu()
        text_menu = Menu()
        text_menu.add_command(label="Edit", command=edit_text)
        text_menu.add_command(label="Save", command=save_text)
        tag_menu = Menu()
        tag_menu.add_command(label="Edit", command=edit_tags)
        tag_menu.add_command(label="Save", command=save_tags)
        main_menu.add_cascade(label="Text", menu=text_menu)
        main_menu.add_cascade(label="Tags", menu=tag_menu)
 
        root.config(menu=main_menu)
        root.mainloop()
        

notebook = Notes()

note1 = Note("This is my first note in this notebook")

note1.add_tag("1234567890")
note1.add_tag("77777")
note1.add_tag("gfg")
print(note1) 
notebook.add(note1)


note2 = Note("This note is about weather")
note2.add_tag("weather")
note2.add_tag("autumn")
print(note2)
notebook.add(note2)


note_weather = notebook.find("weather")
print(note_weather['text'])
    # Видалення запису Jane
notebook.edit_note(note_weather)
#notebook.delete(note_weather)
print(notebook)
