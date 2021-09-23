# задание 1
print('задание_1')

def main():
    num1 = int(input('Введите значение числа 1 '))
    num2 = int(input('Введите значение числа 2 '))

    try:
        result = num1/num2
    except ZeroDivisionError:
        num2 == 0
        print('Неправильный ввод: деление на 0')
        return main ()
    else:
        print('Результат деления числа', num1, 'на число',
          num2, 'равен', format(result, '.2f'))
main ()
...

# задание 2
print('задание_2')

def all_parameters(name, surname, birthyear, city, email, phone):
    print ('Имя:' + name,
           'Фамилия:'+ surname,
           'Год рождения:' + birthyear,
           'Место рождения:' + city,
           'Адрес электронной почты:'+ email,
           'Телефон:'+ phone
           )

all_parameters('Иван','Чай','2010','Тула', 'pochta@m.ru', '2128506')
...

# задание 3
print('задание_3')
def my_func ():
    a = int(input('Введите значение числа a '))
    b = int(input('Введите значение числа b '))
    c = int(input('Введите значение числа c '))
    if a < b:
        min = a
    else:
        min = b
    if c < min: min = c
    result = a + b + c - min
    print('Сумма двух наибольших значений =', result)
my_func ()
...

# задание 4
print('задание_4')

def main():
    x = abs(int(input('Введите значение числа x ')))
    y = int(input('Введите значение числа y '))
    my_func (x,y)

def my_func (x, y):
    result = x**y
    print('Значение', x, 'в степени', y, '=', result)

main ()
...

#задание 5
#print('задание_5')
#s = 0
    #while True:
        #i= input('Введите число ').split()

        #while s < len(i):
            #try:
                #i[s] = int(i[s])
                #s = s + i
                #print(s)

            #except s == '#':
            #break

...

# задание 6
print('задание_6')

input_letters = input('Введите слово ')
def int_func():
    result = input_letters.title()
    print(result)
int_func()

input_string = input('Введите строку ')
new_string = input_string.split()
for i in new_string:
    int_func()
