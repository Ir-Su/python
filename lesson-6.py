# задание 1
print('задание_1: светофор')

import time
class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    def run(self):
        n = 0
        while n < 3:
            print('Горит', (self.__color[n]), 'свет')
            if n == 0:
                time.sleep(7)
                n +=1
                if n != 1:
                    print('Сбой системы')
                    break
            elif n == 1:
                time.sleep(2)
                n += 1
                if n != 2:
                    print('Сбой системы')
                    break
            elif n == 2:
                time.sleep(5)
                n -= 2
                if n != 0:
                    print('Сбой системы')
                    break

light = TrafficLight()
light.run()
...


# задание 2
print('задание_2: асфальтовое покрытие')

class Road:
    def __init__(self, length, wide, asfmass, asfhigh):
        self._length = length
        self._wide = wide
        self.asfmass = asfmass
        self.asfhigh = asfhigh
    def mass(self):
        print (self._length*self._wide*self.asfmass*self.asfhigh)

total = Road(20, 5000, 25, 0.05)
total.mass()

# задание 3
print('задание_3: работник')
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())

ask = Position ('John', 'Don', 'worker', 100, 20)
print(ask.get_full_name())
print(ask.position)
print(ask.get_total_income())
...

# задание 4
print('задание_4: автомобиль')

class Car:

    def __init__(self, car_name, car_color, car_speed, is_police):
        self._car_name = car_name
        self._car_color = car_color
        self._car_speed = car_speed
        self.__is_police = is_police


    def on_car_start(self, car_name, car_color, car_speed, is_police):
        print((self._car_name), 'начинает движение')

    def on_car_stop(self, car_name, car_color, car_speed, is_police):
        print((self._car_name), 'останавливается')

    def on_car_turnright(self, car_name, car_color, car_speed, is_police):
        print((self._car_name), 'поворачивает направо')

    def on_car_turnleft(self, car_name, car_color, car_speed, is_police):
        print((self._car_name), 'поворачивает налево')

    def get_car_speed(self):
        return self._car_speed

my_car = Car('Tesla', 'gray', 100, 'no')
my_car.on_car_start('Tesla', 'gray', 100, 'no')
print(my_car.get_car_speed())

class TownCar(Car):

    def __init__(self, car_name, car_color, car_speed, is_police):
        super().__init__(car_name, car_color, car_speed, is_police)

    def get_car_speed(self):
        return self._car_speed

        if self._car_speed > 60:
            print ('Превышение скорости')

opel = TownCar('Opel', 'gray', 120, 'no')
print(opel.on_car_turnleft('Opel', 'gray', 120, 'no'))
print(opel.get_car_speed())
...

# задание 5
print('задание_5: запуск отрисовки')

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки. Работает', (self.title))

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки ручкой, в работе', (self.title))

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки карандашом, в работе', (self.title))

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки маркером, в работе', (self.title))

note = Stationary('маркер')
note.draw()
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
pen.draw()
pencil.draw()
handle.draw()