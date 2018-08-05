import math


a = 4.4
b = 4.5
e = 0.00001
n = 0

while e < abs(a-b):
    c = (a + b)/2
    if math.tan(c) == c:
        break
    elif math.tan(a) * math.tan(c) > c*c:
        b = c
    else:
        a = c
    n = n + 1
    print(f'{n} - a = {a}, b = {b}, c = {c}')

