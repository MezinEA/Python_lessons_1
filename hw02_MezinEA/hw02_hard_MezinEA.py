# import datetime
#
# __name__ = "Мезин Евгений Александрович"
#
# # Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# # Определить координату y точки с заданной координатой x.
# print('Решение задачи №1')
#
# equation = input('Введите формулу в формате "y = -12x + 11111140.2121" - ')
# x = float(input('Введите значение х = '))
#
# # вычислите и выведите y
#
# # необходимо выделить коэффициенты k и b произвольной длинны
# # для этого найдем все пробелы в заданной формуле и определим их индексы
#
# idx = 0
# idx_list = []
#
# for i in equation:
#     if i == ' ':
#         idx_list.append(idx)
#     idx += 1
#
# # коэффициент k находятся между 2м и 3м пробелом со сдвигом на х
# k = float(equation[idx_list[1]:idx_list[2]-1])
#
# # коэффициент b находятся после 4го пробела
# b = float(equation[idx_list[3]+1:])
#
# answer = k * x + b
#
# print(f'Решением формулы вида y = kx + b является значение - {answer}')
#
#
# ##########################
#
#
# print('Решение задачи №2')
#
# # Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# # Проверить, корректно ли введена дата.
# # Условия корректности:
# # 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
# #  (в зависимости от месяца, февраль не учитываем)
# # 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# # 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# # 4. Длина исходной строки для частей должна быть в соответствии с форматом
# #  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
#
# # # Пример корректной даты
# # date = '01.11.1985'
# #
# # # Примеры некорректных дат
# # date = '01.22.1001'
# # date = '1.12.1001'
# # date = '-2.10.3001'
#
# # date = input('Введите дату в формате dd.mm.yyyy - ')
#
# dict_date = {
#     '01': 'первое',
#     '02': 'второе',
#     '03': 'третье',
#     '04': 'четвертое',
#     '05': 'пятое',
#     '06': 'шестое',
#     '07': 'седьмое',
#     '08': 'восьмое',
#     '09': 'девятое',
#     '10': 'десятое',
#     '11': 'одиннадцатое',
#     '12': 'двенадцатое',
#     '13': 'тринадцатое',
#     '14': 'четырнадцатое',
#     '15': 'пятнадцатое',
#     '16': 'шестнадацтое',
#     '17': 'семнадцатое',
#     '18': 'восемнадцатое',
#     '19': 'девятнадцатое',
#     '20': 'двадцатое',
#     '21': 'двадцать первое',
#     '22': 'двадцать второе',
#     '23': 'двадцать третье',
#     '24': 'двадцать четвертое',
#     '25': 'двадцать пятое',
#     '26': 'двадцать шестое',
#     '27': 'двадцать седьмое',
#     '28': 'двадцать восьмое',
#     '29': 'двадцать девятое',
#     '30': 'тридцатое',
#     '31': 'тридцать первое'
# }
#
# dict_month = {
#     '01': 'Января',
#     '02': 'Февраля',
#     '03': 'Марта',
#     '04': 'Апреля',
#     '05': 'Мая',
#     '06': 'Июня',
#     '07': 'Июля',
#     '08': 'Августа',
#     '09': 'Сентября',
#     '10': 'Октября',
#     '11': 'Ноября',
#     '12': 'Декабря'
# }
#
# date = input('Введите дату в формате dd.mm.yyyy: ')
#
# day = date[:2]
# month = date[3:5]
# year = date[6:]
#
# sim_number = 0
#
# for sim in date:
#     if (sim_number == 2) or (sim_number == 5):
#         if sim != '.':
#              print('Введена некорректная маска ввода')
#     sim_number +=1
#
#
#
# days_31 = {1, 3, 5, 7, 8, 10, 12}
# days_30 = {2, 4, 6, 9, 11}
#
#
# try:
#     int_day = int(day)
#     int_month = int(month)
#     int_year = int(year)
# except:
#     print('Введены некорректные символы')
#
# if ((int_day < 1) or
#         (int_day > 31 and days_31.intersection({int_month})) or
#         (int_day > 30 and days_30.intersection({int_month})) or
#         (int_year < 1 or int_year > 9999)):
#             print('Введен не корректное число, месяц или год. Проверьте правильность ввода.')
# else:
#     print(f'Вы ввели: {str(dict_date.get(day)).capitalize()} {dict_month.get(month)} {year} года')
#
# datetime.datetime.strptime()

print('Решение задачи №3')
# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

max_flat_number = int(input('Введите номер комнаты: '))

# определим переменные
floor = 0
count = 1
flat_number = 0
prefloor_count = True
tower = []

# расставим квартиры на этаже
while True:
    floor += 1
    tower.append([])
    flat = 0
    while True:
        flat += 1
        if flat <= count:
            flat_number +=1
            tower[floor-1].append(flat_number)
            if flat_number == max_flat_number:
                break
        else:
            break
    # определим сколько квартир на этаже для увеличения их количества
    # исключение составляет первый этаж - у него нет предыдущего
    count = len(tower[floor - 1])
    if count == 1:
        count += 1
    else:
        for i in range(count):
            if (count == len(tower[floor - 1 - i])):
                prefloor_count = True
            else:
                prefloor_count = False
        if prefloor_count:
            count += 1

    if flat_number >= max_flat_number:
        break

# нарисуем башню (опционально для удобства проверки)
for i in tower[::-1]:
    print(i)

print(f'Квартира с номером {flat_number} находится слева {flat}-ой на {floor} этаже')


