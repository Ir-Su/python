# задание 1
print('задание_1: расчет заработной платы')

def main():
    hours = float(input('Введите количество отработанных часов: '))
    hourly_pay = float(input('Введите оплату в час, руб.: '))
    bonus = float(input('Введите сумму премии, руб.: '))
    show_income(hours, hourly_pay, bonus)

def show_income(hours, hourly_pay, bonus):
    income = (hours * hourly_pay) + bonus
    print('Заработная плата составляет: ', format(income, '.2f'), 'рублей')

main()
...

# задание 2
print('задание_2: числа больше предыдущего')

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
comp_list = [el for num, el in enumerate(my_list, -1) if my_list[num] > my_list[num -1]]
print(comp_list)
...

# задание 3
print('задание_3: кратные 20 или 21')

print([i for i in range (19,241) if i%20 == 0 or i%21 == 0])
...

# задание 4
print('задание_4: нет повторений')

a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print ([i for i in a if a.count(i) == 1])
...

# задание 5
print('задание_5: перемножить от 100 до 1000')

from functools import reduce

def func(num1, num2):
    return num1 * num2

result = reduce(func, [num for num in range (100,1001) if num%2 == 0], 100)
print (result )
...

# задание 6
print('задание_6: итератор целых чисел')
#скрипт_1
print('скрипт_1')
import itertools

for i in itertools.count(3):
    print (i)
    if i >= 10:
        break
...

#скрипт_2
print('скрипт_2')

from itertools import cycle

repeat = [1, 2, 3]
for i, x in enumerate(itertools.cycle(repeat)):
    print(x)
    if i == 8:
        break
...

# задание 7
print('задание_7: факториал')
#вар 1
import math
print (math.factorial(4))

#вар 2
n = int(input())

fact = 1
for el in fact(n):
    yield fact *= n
    n -= 1

print(next(fact))
