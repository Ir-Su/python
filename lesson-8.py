# задание 1
print('задание_1: ввод даты')

class Date:

    def __init__(self, день=0, месяц=0, год=0):
        self.день = день
        self.месяц = месяц
        self.год = год

    def __repr__(self):
        return f'{self.день} - {self.месяц} - {self.год}'

    @classmethod
    def date_from_input(cls, date_input):
        день, месяц, год = map(int, date_input.split('-'))
        date = cls(день, месяц, год)
        return date

    @staticmethod
    def date_valid(date_input):
        день, месяц, год = map(int, date_input.split('-'))
        return день <= 31 and месяц <= 12 and год <= 2199

test_date1 = Date('20-09-2021')
print(test_date1)
test_date2 = Date.date_from_input('21-09-2021')
print(test_date2)
print(Date.date_from_input('22-09-2021'))
is_valid_date = Date.date_valid('20-14-2021')
print(is_valid_date)
# при тестировании из класса записываются нули, а дальше ОК
...

# задание 2
print('задание_2: создание исключения деления на ноль')
class ZDivErr(Exception):
    def __init__(self, b):
        self.b = b

def main():
    a = int(input('Введите значение числа a '))
    b = int(input('Введите значение числа b '))

    try:
        result = a/b
        if b == 1:
            raise ZDivErr ('Неправильный ввод: деление на 0')
    except ZDivErr as err:
        print(err)
        return main ()
    else:
        print(f'Результат деления числа {a} на число {b} равен {result}')
main ()

#пришлось ошибочное значение b условно принять за единицу - иначе
#реализуется встроенный запрет деления на ноль

...

# задание 3
print('задание_3: создание исключения проверки чисел')
class NumError(Exception):
    def __init__(self, txt):
        self.txt = txt

def main():
    input_num = input('Введите число. Если ввод закончен, наберите \'stop\': ')
    my_list = []
    if input_num != 'stop':
        while True:
            input_num.isdigit()
            try:
                num = float(input_num)
                return main()
            except NumError as err:
                print(err)
                return main()
        else:
            raise NumError('Ошибка: это не число. Попробуйте снова')
    my_list = list(map(int, input()))
    print(my_list)

main()
#числа вводятся прекрасно, а список не формируется ((
...


# задание 4, 5, 6
print('задание_4, 5, 6: склад оргтехники')

class Склад:
    def __init__(self):
        self._dict = {}

    def add_to(self, items):
        self._dict.setdefault(items.group_name(), []).append(items)


class Оргтехника:
    def __init__(self, name, model, number):
        self.name = name
        self.model = model
        self.number = number
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.model} {self.number}'

    def info(self):
        print(f'{self.name} модель:{self.model} количество на складе:{self.number}')

    @classmethod
    def know_number(cls, number):
        print(f'{cls.__name__}.number => {self.number}')

    @staticmethod
    def input_valid():
        print ('Проверьте номер вводимой модели')

class Принтер(Оргтехника):
    def __init__(self, name, model, number, speed):
        super().__init__(name, model, number)
        self.speed = speed

    def info(self):
        print(f'{self.name} модель:{self.model} скорость листов/час:{self.speed} количество на складе:{self.number}')

class Сканер(Оргтехника):
    def __init__(self, name, model, number, lightpower):
        super().__init__(name, model, number)
        self.lightpower = lightpower

    def info(self):
        print(f'{self.name} модель:{self.model} светосила:{self.lightpower} количество на складе:{self.number}')

class Ксерокс(Оргтехника):
    def __init__(self, name, model, number, colorful):
        super().__init__(name, model, number)
        self.colorful = colorful

    def info(self):
        print(f'{self.name} модель:{self.model} цветной:{self.colorful} количество на складе:{self.number}')

орг_1 = Оргтехника ('принтер', '2010', 72)
орг_1.info()
принтер = Принтер ('принтер', '2020', 50, 10)
принтер.info()
сканер = Сканер ('сканер', '2005', 15, 1000)
сканер.info()
ксерокс = Ксерокс ('ксерокс', '2000', 2, 'да')
ксерокс.info()

test =  Оргтехника
test.input_valid()
test =  Оргтехника ('принтер', '2010', 72)
test.know_number()

склад = Склад
склад.add_to(принтер)
склад.add_to(сканер)
склад.add_to(ксерокс)
print(склад._dict)
...

# задание 7
print('задание_7: сложение и умножение комплексного числа')

class Complex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, Complex):
            other = other.__complex

        complex_ = self.__complex + other
        return Complex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, Complex):
            other = other.__complex

        complex_ = self.__complex * other
        return Complex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


a1 = Complex(1, 2)
a2 = Complex(3, 4)

print(a1 + a2)
print(a1 * a2)

