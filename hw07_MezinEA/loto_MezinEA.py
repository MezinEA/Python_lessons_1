#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random
import itertools

class Card:
    def __init__(self, name):
        self.name = name
        self.value_list = list(range(1, 99))
        self.card_field = [['', '', '', '', '', '', '', '', ''],
                           ['', '', '', '', '', '', '', '', ''],
                           ['', '', '', '', '', '', '', '', '']]

        # Заполнение карточки пробелами в произвольном порядке
        for i in range(3):
            empty_space = 1
            while empty_space <= 4:
                j = random.randint(0, 8)
                if self.card_field[i][j] != '  ':
                    self.card_field[i][j] = '  '
                    empty_space += 1

        # Формируем список для заполнения с его предварительной сортировкой по возрастанию
        self.card_nums = [[], [], []]
        idx = 98
        for i in range(3):
            for j in range(5):
                idx -= 1
                self.card_nums[i].append(self.value_list.pop(random.randint(0, idx)))
            self.card_nums[i].sort()

        # Заполняем карточку
        for i in range(3):
            for j in range(9):
                if self.card_field[i][j] != '  ':
                    curr_val = self.card_nums[i].pop(0)
                    if curr_val <= 9:
                        self.card_field[i][j] = f' {curr_val}'
                    else:
                        self.card_field[i][j] = f'{curr_val}'


    def change(self, num):
        """ Изменяем карточку удаляя выпавший элемент """

        for i in range(3):
            for j in range(9):
                try:
                    if num == int(self.card_field[i][j]):
                        self.card_field[i][j] = '--'
                except ValueError:
                    pass

    def show(self):
        """ Выводим карточку на печать """

        print(f'-------------{self.name}--------------')
        for i in range(3):
            string = ''
            for j in range(9):
                string = string + str(self.card_field[i][j]) + '  '
            print(string)
        print('-----------------------------------')

    def check_num(self, num):
        """ Проверяем наличие выпавшего номера в карточке """

        for i in self.card_field:
            for j in i:
                try:
                    if num == int(j):
                        return True
                except ValueError:
                    pass

    def check_win(self):
        """ Проверяем карточку на то, вычеркнуты ли все номера """

        for i in self.card_field:
            for j in i:
                if j != '--' and j != '  ':
                    return False
        return True


class Barrel:
    def __init__(self):
        self.value_list = list(range(1, 100))

    def present_value(self, round):
        return self.value_list.pop(random.randint(1, 99 - round))

def user_decision():
    while True:
        decision = input('\n Зачеркнуть цифру? (y/n) - ')
        if decision == 'y':
            if human_card.check_num(num):
                human_card.change(num)
                return

            else:
                print(f'Вы проиграли - цифры {num} в Вашей карточке нет')
                play = False
                return play

        elif decision == 'n':
            return
        else:
            print('Вы ввели некорректный симовл')

# Игра------------------------------------------------------------------------------

play = True
round = 0

barrel = Barrel()
human_card = Card('Евгений')
comp_card = Card('Компьтер')

while play:
    round += 1
    num = barrel.present_value(round)

    print(f'\nНовый бочонок: {num}, осталось {100 - round}\n')

    # Создание карточек
    human_card.show()
    comp_card.show()

    # Ваш ход
    user_decision()

    # Ход компьютера
    if comp_card.check_num(num):
        comp_card.change(num)

    # Проверка выйгрыша
    if human_card.check_win() and comp_card.check_win():
        print('Ничья')
        play = False
    elif human_card.check_win():
        print('Вы выиграли')
        play = False
    elif comp_card.check_win():
        print('Компьютер победил')
        play = False