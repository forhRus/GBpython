


phone_book = []
path = 'phone_book.txt'

def get_lenght_book():
    return len(phone_book)

def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='utf-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))

def save_file():
    global phone_book
    global path
    file = []
    for contact in phone_book:
        file.append(';'.join(contact))
    file = '\n'.join(file)
    with open(path, 'w', encoding='utf-8') as data:
        data.writelines(file)

def get_phone_book():
    global phone_book
    return phone_book

def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)

def delete(contact: str):
    global phone_book
    del phone_book[int(contact)-1]

def change(contact: str, change_contact: list):
    global phone_book
    for i in range(len(change_contact)):
        phone_book[int(contact)-1][i] = change_contact[i]
    phone_book.sort()

def search(find: list):
    result = []
    global phone_book
    for contact in phone_book:
        for field in contact:
            if find in field.lower():
                result.append(contact)
                break
    return result

def make_string_contact(contact):
    return ' '.join(contact)

def get_contact(contact):
    global phone_book
    return phone_book[int(contact)-1]

