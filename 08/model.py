import view
V = view.View
class Book:
    book_list = []
    path: str

    def __init__(self, path: str = 'book.txt'):
        self.path = path
        self.open()

    def open(self):
        with open(self.path, 'r', encoding='utf-8') as data:
            file = data.readlines()
        for expression in file:
            self.book_list.append(expression.strip().split())

    def parse(self, exp):
        exp = exp.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()
        new_exp = [exp[0]]
        for i in range(1, len(exp)):
            if exp[i] + exp[i-1] == '**':
                new_exp[-1] = '**'
            else:
                new_exp.append(exp[i])
        if exp[0] == '-':
            exp[1] = '-' + exp[1]
            exp.pop(0)
        return new_exp


    def make_int_list(self, exp: list):
        list_exp = []
        for i in exp:
            if i.isdigit():
                if int(i) == float(i):
                    list_exp.append(int(i))
                else:
                    list_exp.append(float(i))
            else:
                list_exp.append(i)
        return list_exp

    def solve(self, list_exp: list):
        while True:
            if '(' in list_exp:
                index1 = 0
                index2 = list_exp.index(')')
                for i in range(len(list_exp)):
                    if list_exp[i] == '(':
                        index1 = i
                        if list_exp[i] == ')':
                            break
            else:
                ans = self.func(list_exp)
                ans[0] = str(ans[0])
                return ans
            list_exp[index1] = self.func(list_exp[index1+1:index2])[0]
            del list_exp[index1+1:index2+1]

    def func(self, list_exp):
        exp = list_exp.copy()
        operation = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: x / y,
                     '**': lambda x, y: x ** y}
        def calc(operator_1, operator_2):
            i = 0
            while operator_1 in list_exp or operator_2 in list_exp:
                if list_exp[i] in [operator_1, operator_2]:
                    list_exp[i - 1] = operation.get(list_exp[i])(float(list_exp[i - 1]), float(list_exp[i + 1]))
                    list_exp.pop(i)
                    list_exp.pop(i)
                else:
                    i += 1
        calc('**','**')
        calc('*', '/')
        calc('+', '-')
        if list_exp[0] == int(list_exp[0]):
            list_exp[0] = int(list_exp[0])
            return list_exp
        else:
            return list_exp

    def save(self, exp: list, answer: list):
        self.book_list.append(exp + answer)
        if len(self.book_list) > 1:
            string = '\n' + ' '.join(self.book_list[-1])
        else:
            string = ' '.join(self.book_list[-1])
        with open(self.path, 'a', encoding='utf-8') as data:
            data.writelines(string)

    def update(self):
        string = []
        for exp in self.book_list:
            string.append(' '.join(exp))
        string = '\n'.join(string)
        with open(self.path, 'w', encoding='utf-8') as data:
            data.writelines(string)

    def delete(self, ch):
        del self.book_list[ch-1]
        self.update()

    def clear(self):
        self.book_list.clear()
        self.update()



