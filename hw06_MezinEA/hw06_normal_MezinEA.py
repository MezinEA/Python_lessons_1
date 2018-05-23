# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


import generation_modul as gm

class School:
    school_name = "1st man's middle school of Perm city"
    grade_list = []


class Grade(School):
    def __init__(self, number):
        self.number = number
        School.grade_list.append(number)
        self.apprentice_list = []
        self.teacher_list = []


class Teacher(School):
    def __init__(self, teacher_name, subject, grade):
        self.teacher_name = teacher_name
        self.subject = subject
        self.grade = grade.number
        grade.teacher_list.append(self.teacher_name)


class Apprentice(Grade):
    def __init__(self, child_name, mother_name, father_name, grade):
        self.child_name = child_name
        self.mother_name = mother_name
        self.father_name = father_name
        self.grade = grade.number
        grade.apprentice_list.append(self.child_name)


grade_init_dict = {}
for i in range(11):
    for j in range(4):
        letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
        grade_init_dict[f'{i+1}_{letter.get(j)}'] = Grade(f'{i+1}_{letter.get(j)}')


# Заполняем учеников по классам
app_list = []
for i in range(11):
    for j in range(4):
        letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
        for m in range(15):
            app_list.append(Apprentice(gm.rand_fio(), gm.rand_fio(), gm.rand_fio(), grade_init_dict.get(f'{i+1}_{letter.get(j)}')))


subject_list = ['математика', 'русский язык', 'литература', 'география', 'химия', 'физика', 'биология', 'ОБЖ',
                'физкультура', 'рисование', 'пение', 'естествознание', 'информатика']

# Создание и расстановка преподавателей по классам
teach_list = []
for i in range(11):
    for j in range(4):
        letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
        for m in subject_list:
            teach_list.append(Teacher(gm.rand_fio(), m, grade_init_dict.get(f'{i+1}_{letter.get(j)}')))

# Основная программа
while True:
    key = input('\n\n\n '
                'Введите номер команды: \n'
                '1. Получить полный список всех классов школы. \n'
                '2. Получить список всех учеников в указанном классе \n'
                '3. Получить список всех предметов указанного ученика \n'
                '4. Узнать ФИО родителей указанного ученика \n'
                '5. Получить список всех Учителей, преподающих в указанном классе \n'
                '0. Выход из приложения \n')

    if key == '1':
        print(School.grade_list)
    elif key == '2':
        grade_num = input('Введите название класса: ')
        try:
            print(grade_init_dict.get(grade_num).apprentice_list)
        except AttributeError:
            print('Такого класса не существует. Посмотрите список классво (команда 1)')
    elif key == '3':
        app_name = input('Введите имя ученика: ')
        sub_list = []
        for i in app_list:
            if app_name == i.child_name:
                for teach in grade_init_dict.get(i.grade).teacher_list:
                    for j in teach_list:
                        if teach == j.teacher_name:
                            sub_list.append(j.subject)
        if sub_list != []:
            print(sub_list)
        else:
            print('Такой ученик не найден')
    elif key == '4':
        app_name = input('Введите имя ученика: ')
        fail = True
        for i in app_list:
            if app_name == i.child_name:
                print('Можно сделать лучше: '
                      '\n 1 На основании имени отца - сопоставлять отчество'
                      '\n 2 Делать раздельно полые браки'
                      'Но т.к. задача normal - 99% будут усыновлять и 50% будут "Евро семьи"')
                print(f'Отца зовут - {i.father_name}')
                print(f'Мать зовут - {i.mother_name}')
                fail = False
        if fail:
            print('Такой ученик не найден')
    elif key == '5':
        grade_num = input('Введите название класса: ')
        try:
            print(grade_init_dict.get(grade_num).teacher_list)
        except AttributeError:
            print('Такого класса не существует. Посмотрите список классво (команда 1)')
    elif key == '0':
        print('До скорых встреч')
        break
    else:
        print('Вы ввели несуществующую команду')