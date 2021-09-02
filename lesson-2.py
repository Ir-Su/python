# задание 1
print('задание_1')
# вар 1
my_list = (45, 'Hello', 3.7, None)
def f(el):
    for el in range(len(my_list)):
        print(f"element '{el}' is {type(my_list[el])}")
    return
f(my_list)
# вар 2
my_list = (45, 'Hello', 3.7, None)
print(list(map(type, my_list)))

# задание 2
print('задание_2')
l = [1, 2, 3, 4]
l[::2], l[1::2] = l[1::2], l[::2]
print(l)

# задание 3
print('задание_3')
# вар 1
month = int(input('Введите номер месяца '))
seasons_list = ('зима', 'весна', 'лето', 'осень')
if month == 1 or month == 2 or month == 12:
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
# вар 2
month = int(input('Введите номер месяца '))
seasons_dict = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
for key in seasons_dict.keys():
    if month in seasons_dict[key]:
        print(key)

# задание 4
print('задание_4')
str = input('Введите строку ').split()
for i, word in enumerate(str):
    print(word[0:10])

# задание 5
print('задание_5')
my_list = [2, 3, 3, 5, 7]
print('Рейтинг:', (my_list))
new_input = int(input('Введите значение рейтинга '))
for el in range(len(my_list)):
    if new_input == el:
        my_list.insert(el - 1, new_input)
    elif new_input < min(my_list):
        my_list.insert(new_input, min(my_list))
    elif new_input > max(my_list):
        my_list.insert(max(my_list), new_input)
        print('Новый рейтинг:', (my_list)).split()

# задание 6
print('задание_6')
analysis = int(input('Число товаров для анализа '))
(N)= analysis
i = 0
order = input('Порядковый номер ')
name = input('Название товара ')
price = input('Цена товара ')
num = input('Количество товара ')
units = input('Единицы измерения количества ')
i += 1
my_dict = {'Название': (name), 'цена': (price), 'количество': (num), 'шт': (units)}
while i >= N:
    list = ()
    for value in my_dict.values():
        list = sum(my_dict.values()). split()
        for key in my_dict.items():
        print(key, list)