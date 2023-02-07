import view
import model as m
J = m.Jurnal()
V = view.View()
def start():
    while True:
        # flag_done = False
        V.show_menu()
        choice = V.validate_input_choice('Выберите пункт меню: ', 1, V.length_menu)
        if choice == 1:  # "добавить нового ученика"
            pupil = V.input_pupil()
            J.add_pupil(pupil)
            V.print_message(f'Ученик(ца) "{pupil}" добавлен(а) в класс')
        elif choice == 2:  # 'Добавить предмет'
            lesson = V.input_lesson("Введите название нового предмета: ", 'Такой предмет уже есть.', J.scooll_lessons)
            if lesson:
                J.add_lesson(lesson)
                V.print_message(f'Новый предмет "{lesson}" добавлен в программу')
        elif choice == 3:  # 'Добавить оценку ученику'
            pupil = V.validate_contain('Какому ученику вы хотите добавить оценку: ', 'В журнале нет такого ученика.', J.pupils)
            if pupil:
                lesson = V.validate_contain('Укажите предмет: ', 'В учебной программе нет такого предмета', J.scooll_lessons)
                if lesson:
                    grade = str(V.validate_input_choice('Оценка: ', 2, 5))
                    J.add_grade(pupil, lesson, grade)
        elif choice == 4:  #  "Показать список учеников"
            V.show_pupils(J.jurnal_dict)

        elif choice == 5:  # "Показать оценки ученика"
            pupil = V.validate_contain('Оценки какого ученика вы хотите посмотреть: ', 'В журнале нет такого ученика.',
                                       J.pupils)
            if pupil:
                V.show_rate(J.jurnal_dict, pupil)

        elif choice == 6:
            J.generate_class(30, 5, 7, 5)

        elif choice == 7:  # "выход"
            break
        # print(J.jurnal_dict)
        # print(J.scooll_lessons)
        J.update()