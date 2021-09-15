# задание 1
print('задание_1: создать файл')
my_file = open('home5task1.txt', 'w')
line = input('Введите данные ')
while line:
    my_file.writelines(line)
    line = input('Введите данные ')
    if not line:
        break
my_file.close()
...

# задание 2
print('задание_2: подсчет строк')
my_file = open('home5task2.txt', 'r')
my_file.seek(0)
content = my_file.read()
print(f'Содержимое файла: {content}')
my_file = open('home5task2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк:  {len(content)}')
my_file = open('home5task2.txt', 'r')
content = my_file.read()
content = content.split()
print (f'Количество слов  {len(content)}')
my_file.close()
...

# задание 3
print('задание_3: вычисление зарплаты из файла')
with open('home5task3_salary.txt', 'r') as f_obj:
        workers = {}
        for line in f_obj:
            key, value = line.split()
            workers[key] = value
            if int(value) < 20000:
                print(f'{key} зарплата меньше 20000')
        print (f'средний оклад {sum(map(int, value)) / len(value)}')
...

# задание 4
print('задание_4: числительные')
#вар 1
translation = {'One': 'Один' , 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open ('home5task4_trans.txt', 'r') as f_obj:
    new = []
    for i in f_obj:
        i = i.split(' ', 1)
        new.append(translation[i[0]] + ' ' + i[1])
print(new)

#вар 2
translation = {'One': 'Один' , 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open ('home5task4_trans.txt', 'r') as f_obj:
    new = {}
    for line in f_obj:
        key, value = line.split('–')
        new[key] = translation[value]
        print(f'{new[key]} - {f_obj[key]}')
#но это элегантное решение не прошло ))
...

# задание 5
print('задание_5: сумма чисел')
def sum_line():
        with open('home5task5.txt', 'w') as f_obj:
            line = input('Введите числа через пробел ')
            f_obj.writelines(line)
            new_line = line.split()
            print(sum(map(int, new_line)))
sum_line()
...

# задание 6
print('задание_6: сумма чисел')
lessons = {}
with open('home5task6.txt', 'r') as f_obj:
    for line in f_obj:
        subject, lect, pract, labs = line.split()
        lessons[subject] = (int(lect) + int(pract) + int(labs))
    print(f'Количество часов по предмету - {lessons}')
...

# задание 7
print('задание_7: фирма')
import json
import math

profit = {}
totalprofit = 0
i = 1

with open ('home5task7.txt', 'r') as file:
    for line in file:
        name, private, income, outcome = line.split()
        profit[name] = int(income) - int(outcome)
        if profit.setdefault(name) >= 0:
            totalprofit = totalprofit + profit.setdefault(name)
            print(f'Фирма {name}: {profit.setdefault(name): .1f}')
            i += 1
        else:
            print(f'Фирма {name} не получила прибыль, убыток {profit.setdefault(name)}')
            i -= 1
    if i != 0:
        average_profit = totalprofit / (i)
        print(f'Средняя прибыль: {average_profit : .1f}')

with open ('home5task7.json', 'w') as js_file:
    json.dump(profit, js_file)

    js_str1 = json.dumps(profit)
    print(f'{js_str1}')
    js_str2 = json.dumps(average_profit)
    print(f'average {js_str2}')

