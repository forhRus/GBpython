
class View:
    main_menu = ['Ввести арифметическое выражение',
                'Записать выражение в книгу',
                'Показать имеющиеся выражения',
                'Показать ответ выражения',
                'Удалить выражение из книги',
                'Очистить книгу',
                'Выход']
    length = len(main_menu)

    def show_main_menu(self):
        print('Главное меню:')
        for i, item in enumerate(self.main_menu, 1):
            print(f'\t{i}. {item}')
        print()
        while True:
            try:
                choice = int(input('Выберите пункт меню: '))
                print()
                if 0 < choice <= self.length:
                    return choice
                else:
                    self.print_message(f'Необходимо ввести число от 1 до {self.length}')
            except ValueError:
                print()
                self.print_message('Введите корректное значение')

    def expression_input(self):
        exp = input('Введите выражение: ')
        print()
        return exp

    def print_solve(self, exp: list, ans: list):
        print(' '.join(exp), '=', *ans)
        print()

    def check_parentheses(self, exp_list: list):
        if exp_list.count('(') == 0 and exp_list.count(')') == 0:
            return True
        elif exp_list.count('(') != exp_list.count(')'):
            self.print_message('Ошибка в количестве скобок.')
            return False
        else:
            temp_string = ''
            for i in exp_list:
                if i in '()':
                    temp_string += i
            while '()' in temp_string:
                temp_string = temp_string.replace('()', '')
                print(temp_string)
            if len(temp_string):
                self.print_message('Допущена ошибка в порядке скобок')
                return False
            else:
                return True

    def check_save(self, book, exp, ans):
        temp = exp + ans
        if temp in book:
            self.print_message('Такое выражение уже записано в книге')
            return False
        else:
            return True

    def print_message(self, msg):
        print(msg)
        print()

    def show_book(self, book):
        if book:
            print('Ваша книга')
            for i, expression in enumerate(book, 1):
                print(f'\t{i}.', *expression[:-1])
            print()
        else:
            self.print_message('Книга пока что пуста')

    def show_answer(self, book):
        length = len(book)
        while True:
            ch = input(f'В книге всего {length} выражений. Ответ какого выражения вы хотите увидеть (n - для выхода в меню): ')
            print()
            if ch == 'n':
                break
            elif self.validate_choice_book(ch, length):
                print(*book[int(ch)-1][:-1], '=',book[int(ch)-1][-1])
                print()

    def in_ch_del_exp(self,book):
        length = len(book)
        while True:
            ch = input(f'В книге всего {length} выражений. Какое выражение вы хотите удалить (n - выход в меню): ')
            print()
            if ch == 'n' or self.validate_choice_book(ch, length):
                return ch

    def validate_choice_book(self, ch, length):
        if length:
            if ch.isdigit() and int(ch) in range(1, length + 1):
                return True
            elif not ch.isdigit():
                self.print_message('Необходимо ввести номер выражения.')
                return False
            else:
                self.print_message('В книге нет выражения с таким номером.')
                return False
        else:
            self.print_message('Ваша книга пуста.')
            return False

    def input_agree(self, msg: str):
        choice = input(msg).lower()
        print()
        if choice == 'y':
            return True
        return False





