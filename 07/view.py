commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход']

def main_menu():
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    while True:
        try:
            print()
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 9:
                print()
                return choice
            else:
                print('Необходимо ввести число от 1 до 8')
        except ValueError:
            print('Введите корректное значение')

def file_opened():
    print('Файл успешно открыт')
    print()

def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не октрыта')
    else:
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:12} {contact[2]:20}')
    print()

def save_book():
    print('Изменения сохранены')
    print()

def create_new_contact():
    chars = ['all', 'digit']
    max_lenght = {'name': 20, 'phone': 10, 'comment': 20}
    while True:
        name = input('Введите имя и фамилию:  ')
        if validate_create(name, chars[0], max_lenght['name']):
            print()
            break
        else:
            print_message('Превышена максимальная длина в 20 символов.')
    while True:
        phone = input('Введите телефон (без 8, максимальная длина 10 символов): ')
        if validate_create(phone, chars[1], max_lenght['phone']):
            print()
            break
        else:
            print_message('Ошибка ввода')
    while True:
        comment = input('Ввведите комментарий: ')
        if validate_create(comment, chars[0], max_lenght['comment']):
            print()
            break
        else:
            print_message('Превышена максимальная длина в 20 символов.')
    print()
    return name, phone, comment

def validate_create(inter, chars, lenght):
    if chars == 'all' and len(inter) <= lenght:
        return True
    elif  chars == 'digit' and inter.isdigit() and 0 < int(inter) and len(inter) <= lenght:
        return True
    return False

def contact_created(contact):
    print(f'Создан контакт "{contact}"')
    print()

def delete_contact():
    contact = input('Введите номер контакта, который вы хотите удалить: ')
    print()
    return contact

def contact_deleted(result):
    print(f'Контакт "{result}" удалён')
    print()

def change_contact():
    contact = input('Введите контакт, который вы хотите изменить: ')
    print()
    return contact

def validate_change(contact, lenght):
    if contact.isdigit() and 0 < int(contact) <= lenght:
        return True
    elif contact.isalpha():
        print('Ошибка ввода')
    else:
        print('Контакта с таким номером не существует')
    print()
    return False

def contact_changed(contact, changed_contact):
    print(f'Контакт "{contact}" изменён на "{changed_contact}"')
    print()

def find_contact():
    find = input('Найти: ')
    return find

def print_message(msg):
    print()
    print(msg)
    print()

def end_program():
    print('До свидания. Программа завершена.')

