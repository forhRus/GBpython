from note import Note
from datetime import datetime
from noteBook import NoteBook
class Model:
    __pathNoteBook = 'notebook.csv'
    __idNote = 0
    __noteBook = NoteBook()
    def __init__(self):
        self.load()

    def createNote(self, title: str, body: str):
        self.__idNote += 1
        time = datetime.now()
        newNote = Note(self.__idNote, title, body, time)
        self.__noteBook.add(newNote)

    def getNoteList(self):
        return self.__noteBook.getList()

    def save(self):
        saveString = []
        saveString.append(str(self.__idNote))
        for n in self.__noteBook.getList():
            strNote = self.__stringNote(n)
            saveString.append(strNote)
        with open(self.__pathNoteBook, 'w', encoding='utf-8') as data:
            data.write('\n'.join(saveString))

    def __stringNote(self, n: Note):
        return f'{n.getId()};{n.getTitle()};{n.getBody()};{n.getDate()}'

    def load(self):
        with open(self.__pathNoteBook, 'r') as data:
            file = data.readlines()
        if file:
            self.__idNote = int(file[0])  #  вытаскиваем крайний id
            for i in range(1, len(file)):
                self.__noteBook.add(self.__parsLine(file[i]))  #  выгружаем заметки из файла

# парсим заметку
    def __parsLine(self, line: str):
        n = line.strip().split(";")
        note = Note(int(n[0]), n[1], n[2], n[3])
        return note

    def getCountId(self):
        return self.__idNote

    def checkId(self, id: int):
        for note in self.__noteBook.getList():
            if note.getId() == id:
                return True
        return False

    def findIndex(self, id: int):
        index = self.__noteBook.find(id)
        return index

    def deleteNote(self, index: int):
        self.__noteBook.delete(index)

    def swap(self, index: int, title: str, body: str):
        note = self.__noteBook.getNote(index)
        note.setTitle(title)
        note.setBody(body)
        note.setDate(datetime.now())
        self.__noteBook.swap(index)









