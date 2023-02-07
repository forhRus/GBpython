
class View:
    main_menu = ["Добавить ученика в класс",
         "Добавить предмет",
         "Добавить оценку ученику",
         "Показать список учеников",
         "Показать оценки ученика",
         "Сгенерировать класс из 30 учеников, 5 предметов, до 10 оценок",
         "Выход из программы"]
    length_menu = len(main_menu)
    def show_menu(self):
        print('Главное меню.')
        for i, item in enumerate(self.main_menu, 1):
            print(f'\t{i}. {item}')
        print()
    def input_pupil(self):
        last_name = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        print()
        pupil = f'{last_name} {first_name}'
        return pupil
    def input_lesson(self, msg1: str, msg2: str, col):
        name_lesson = input(msg1)
        for item in col:
            if name_lesson.lower() in item.lower():
                self.print_message(msg2)
                name_lesson = False
                break
        else:
            return name_lesson
    def validate_input_choice(self, msg: str, m1: int, m2: int):
        while True:
            try:
                choice = int(input(msg))
                print()
                if m1 <= choice <= self.length_menu:
                    return choice
                else:
                    self.print_message(f'Необходимо ввести число от {m1} до {m2}')
            except ValueError:
                print()
                self.print_message('Введите корректное значение')
    def print_message(self, msg):
        print(msg)
        print()
    def show_pupils(self, jurnal: list):
        for i, p in enumerate(jurnal, 1):
            print(f'{i}. {p}')
    def validate_contain(self, msg1: str, msg2: str, col):
        name = input(msg1)
        for item in col:
            if name.lower() in item.lower():
                return item
        else:
            self.print_message(msg2)
            name = False
    def show_rate(self, jurnal: list, pupil: str):
        print(pupil)
        for l in jurnal[pupil]:
            print(f'\t{l}: ', end='')
            print(*jurnal[pupil][l], sep=',')




