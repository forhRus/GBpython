import random
import random as r
class Jurnal:
    jurnal_dict = {}
    pupils = []
    scooll_lessons = []
    path_jurnal = 'jurnal.txt'
    def __init__(self):
        if self.pupils:
            for p in self.pupils:
                self.jurnal_dict[p] = {}
                if self.scooll_lessons:
                    for l in self.scooll_lessons:
                        self.jurnal_dict[p][l] = []
    def add_pupil(self, new_pupil: str):
        self.jurnal_dict[new_pupil] = {}
        self.pupils.append(new_pupil)
        if self.scooll_lessons:
            for l in self.scooll_lessons:
                self.jurnal_dict[new_pupil][l] = []
    def add_lesson(self, lesson: str):
        for pupil in self.jurnal_dict:
            self.jurnal_dict[pupil][lesson] = []
        self.scooll_lessons.append(lesson)
    def add_grade(self, pupil, lesson, grade):
        self.jurnal_dict[pupil][lesson].append(grade)
    def update(self):
        save = []
        for p in self.jurnal_dict:
            string = p + '\n'
            for l in self.jurnal_dict[p]:
                if len(self.jurnal_dict[p][l]) > 1:
                    s = ", ".join(self.jurnal_dict[p][l])
                    string += f'{l}: {s}\n'
                elif self.jurnal_dict[p][l]:
                    s = self.jurnal_dict[p][l][0]
                    string += f'{l}: {s}\n'
                else:
                    string += f'{l}:\n'
            save.append(string)
        with open(self.path_jurnal, 'w', encoding='utf-8') as data:
            data.writelines('\n'.join(save))
    def generate_class(self, c_p, c_l, c_m, m):
        p_man = 'name_man.txt'
        p_woman = 'name_woman.txt'
        name1 = []
        name2 = []
        ran_les = ['Физика', 'Физкультура', 'Литература', 'Русский язык', 'Труд', 'Музыка', 'Алгебра', 'Геометрия', 'Биология', 'География', 'Информатика']
        with open(p_man, 'r', encoding='utf-8') as data:
            file = data.readlines()
            for line in file:
                name1 += line.strip().split()
        with open(p_woman, 'r',encoding='utf-8') as data:
            file = data.readlines()
            for line in file:
                name2 += line.strip().split()
        for _ in range(c_p):
            new_pupil = ''
            coin = random.randint(0, 1)
            if coin == 1:
                new_pupil = random.choice(name1)
                last_name = random.choice(name1)
                if last_name[-1] == 'й':
                    last_name = last_name[:-1] + 'ев'
                else:
                    last_name += 'ов'
            else:
                new_pupil = random.choice(name2)
                last_name = random.choice(name1)
                if last_name[-1] == 'й':
                    last_name = last_name[:-1] + 'евa'
                else:
                    last_name += 'овa'
            self.pupils.append(last_name + ' ' + new_pupil)
        self.pupils.sort()
        self.scooll_lessons = [ran_les.pop(ran_les.index(random.choice(ran_les))) for _ in range(c_l)]
        self.__init__()
        for p in self.jurnal_dict:
            for l in self.jurnal_dict[p]:
                self.jurnal_dict[p][l].extend([str(random.randint(2, m)) for _ in range(random.randrange(1, c_m))])





