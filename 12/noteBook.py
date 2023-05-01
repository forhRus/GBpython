from note import Note

class NoteBook():
    __noteBook = []
    __size = 0
    def __init__(self):
        self.__noteBook = []
        self.__size = len(self.__noteBook)

    def add(self, newNote: Note):
        self.__noteBook.insert(0, newNote)

    def getNote(self, index: int):
        note = self.__noteBook[index]
        return note

    def getList(self):
        return self.__noteBook

    def getSize(self):
        return self.__size

    def showList(self):
        print(self.__noteBook)

    def find(self, id: int):
        i = 0
        for Note in self.__noteBook:
            if Note.getId() == id:
                return i
            i += 1

    def delete(self, i: int):
        del self.__noteBook[i]

    def swap(self, index: int):
        self.__noteBook.insert(0, self.__noteBook.pop(index))
