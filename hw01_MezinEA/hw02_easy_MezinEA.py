__name__ = "Мезин Евгений Александрович"

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
from typing import Any, Union

fruit_list = ["яблоко", "банан", "киви", "арбуз"]
n = 1
for i in fruit_list:
    print('{} {:>8}'.format(n, i, 'right aligned'))
    n += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list1 = [1, 4, 6, 2, 4, 3, 6, 3, 3, 3, 3, 3, 7, 8]
list2 = [1, 7, 6, 5, 5, 5, 6, 3]

idx = 0
while idx < len(list1):
    for el in list2:
        if list1[idx] == el:
            list1.pop(idx)
            idx -=1 #pop удаляет элемент, значит необходимо следующий элемет, ставший предыдущим проверить снова
            break
    idx += 1        #каждый круг будет добавляться новый порядок в индекс
print(list1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list3 = [1, 4, 6, 2, 4, 3, 6, 3, 3, 3, 3, 3, 7, 8]
list4 = []

for number in list3:
    if number % 2 == 0:
        list4.append(number / 4)
    else:
        list4.append(number * 2)

print(f'Первоначальный список - {list3}')
print(f'Новый список          - {list4}')