from note import Note
from menu import Menu

class View:
    def showMenu(self, m: Menu):
        print(m.getName())
        for i, item in enumerate(m.getMenu(), 1):
            print(f'\t{i}. {item}')
        print()

    def inputText(self, msg: str, len: int):
        return input(msg)[:len]

    def showList(self, nb: list):
        if len(nb) == 0:
            print("Заметок нет")
        else:
            for i in range(len(nb)):
               print(f'{i+1}. {self.__showNoteShort(nb[i])}')
        print()

    def __showNoteShort(self, n: Note):
        body = n.getBody()
        body = (f'{body[:16]}...' if len(body) > 16 else body)
        return f'id: {n.getId()}, {n.getTitle()}, {body}, {n.getDate()}'

    def showNote(self, n: Note):
        print(f'id: {n.getId()}\n'
              f'title: {n.getTitle()}\n'
              f'body: {n.getBody()}\n'
              f'date: {n.getDate()}\n')

    def validateInputChoice(self, l: int):
        while True:
            try:
                choice = int(input())
                if 1 <= choice <= l:
                    print()
                    return choice
                else:
                    self.printMessage(f'Необходимо ввести число от 1 до {l}')
            except ValueError:
                print()
                self.printMessage('Введите корректное значение')

    def printMessage(self, msg):
        print(msg)






