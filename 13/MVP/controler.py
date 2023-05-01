from MVP import view
from MVP import model
from base.menu import Menu

M = model.Model()
V = view.View()
mainMenu = Menu(["Новая заметка", "Список заметок", "Записать изменения", "Выход"], "Главное меню:")
noteMenu = Menu(["Посмотреть заметку", "Радактировать заметку", "Удалить заметку", "Назад"], "Выберите действие:")
searchMenu = Menu(["Порядковый номер", "ID", "Назад"], "Способ поиска:")
changeMenu = Menu(["Заголовок", "Тело", "Назад"], " Изменить: ")

def start():
    flagsave = False
    while True:
        V.showMenu(mainMenu)
        V.printMessage('Выберите пункт меню: ')

        choice = V.validateInputChoice(mainMenu.getLength())
        if choice == 1:  # "новая заметка"
            title = V.inputText('Заголовок заметки: ', 16)
            body = V.inputText('Текст заметки: ', 100)
            M.createNote(title,body)
            flagsave = True
            V.printMessage(f'Заметка добавлена\n')
        elif choice == 2: # "Список заметок"
            V.printMessage('Список заметок:')
            V.showList(M.getNoteList())
            changeNote()
            flagsave = True
        elif choice == 3: #Запись
            if flagsave:
                M.save()
                V.printMessage("Сохранение прошло успешно\n")
                flagsave = False

        elif choice == mainMenu.getLength():  # "выход"
            if flagsave:
                M.save()
            print('Программа завершена\n')
            break

def changeNote():

    while True:
        if len(M.getNoteList()) == 0:
            "Заметок нет"
            break
        V.showMenu(noteMenu)
        choice = V.validateInputChoice(noteMenu.getLength())
        if choice == mainMenu.getLength(): # "назад"
            break
        index = searchNoteIndex()
        if index >= 0:
            if choice == 1:  # "Посмотреть заметку"
                V.showNote(M.getNoteList()[index])
            elif choice == 2: # "Редактировать заметку"
                title = V.inputText('Заголовок заметки: ', 16)
                body = V.inputText('Текст заметки: ', 100)
                M.swap(index, title, body)
                V.printMessage(f'Заметка изменена\n')
            elif choice == 3: # "Удалить заметку"
                M.deleteNote(index)
                V.printMessage(f'Заметка Удалена\n')
        elif index == -1:
            V.printMessage("Заметки с таким id не существует")

def searchNoteIndex():
    while True:
        V.showMenu(searchMenu)
        V.printMessage("Ваш выбор:")
        choice = V.validateInputChoice(searchMenu.getLength())
        if choice == searchMenu.getLength():  # "назад"
            return -2
        if choice == 1:  # "Порядковый номер"
            V.printMessage("Введите номер заметки: ")
            listNote = M.getNoteList()
            number = V.validateInputChoice(len(listNote))
            return number-1
        elif choice == 2:  # "ID"
            V.printMessage("Введите ID заметки: ")
            id = V.validateInputChoice(M.getCountId())
            if M.checkId(id):
                index = M.findIndex(id)
                return index
            else:
                return -1


