import view
import model

def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()
        if choice == 1:  # открыть файл
            model.open_file()
            view.file_opened()
        elif choice == 2:  # сохранить файл
            model.save_file()
            view.save_book()
        elif choice == 3:  # показать все контакты
            view.show_contacts(model.get_phone_book())
        elif choice == 4:  # создать контакт
            new_contact = list(view.create_new_contact())
            model.add_new_contact(new_contact)
            new_contact = model.make_string_contact(new_contact)
            view.contact_created(new_contact)
        elif choice == 5:  # удалить контакт
            contact = view.delete_contact()
            lenght_book = model.get_lenght_book()
            if view.validate_change(contact, lenght_book):
                del_contact = model.get_contact(contact)
                model.delete(contact)
                del_contact = model.make_string_contact(del_contact)
                view.contact_deleted(del_contact)
        elif choice == 6:  # изменить контакт
            contact = view.change_contact()
            lenght_book = model.get_lenght_book()
            if view.validate_change(contact, lenght_book):
                changed_contact = list(view.create_new_contact())
                model.change(contact, changed_contact)
                contact = model.make_string_contact(contact)
                changed_contact = model.make_string_contact(changed_contact)
                view.contact_changed(contact, changed_contact)
        elif choice == 7:  # найти контакт
            find = view.find_contact()
            result = model.search(find)
            view.show_contacts(result)
        else:
            view.end_program()
            break



