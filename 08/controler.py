import view
import model
V = view.View()
B = model.Book()
def start():
    choice = ''
    flag_done = False
    while True:
        choice = V.show_main_menu()
        if choice == 1:  # 'Ввести арифметическое выражение'
            parse_exp = B.parse(V.expression_input())
            if V.check_parentheses(parse_exp):
                answer = B.solve(B.make_int_list(parse_exp))
                V.print_solve(parse_exp, answer)
                flag_done = True
        elif choice == 2:  # 'Сохранить выражение'
            if flag_done:
                if V.check_save(B.book_list, parse_exp, answer):
                    B.save(parse_exp, answer)
                    V.print_message('Выражение записано в книгу')
            else:
                V.print_message('Вы ещё ничего не ввели.')
        elif choice == 3:  # 'Показать имеющиеся выражения'
            V.show_book(B.book_list)
        elif  choice == 4:  #  показатать ответ выражения
            V.show_answer(B.book_list)
        elif choice == 5:   #  удалить выражение из книга
            ch = V.in_ch_del_exp(B.book_list)
            if ch.isdigit():
                B.delete(int(ch))
                V.print_message('Выражение удалено.')
        elif choice == 6:  # очистить книгу
            if V.input_agree('Вы уверены что хотите очистить книгу (y/n):'):
                B.clear()
                V.print_message('Книга очищена.')
        elif choice == 7:  # выход
            if flag_done and not parse_exp+answer in B.book_list:
                if V.input_agree('Выражение не записано в книгу. Вы точно хотите выйти? (y/n): '):
                    break
            else:
                break


