# задание 1
print('задание_1: сложение матриц')

class Matrix:
    def __init__(self, A):
        self.A = А[i][j]
        self.B = '\n'.join(['\t'.join([str(j) for j in i]) for i in A])

    def __add__(self, other):
        NumStr = len(self.A)
        NumCol = len(other.A[0])
        for i in range(NumStr):
            for j in range(NumCol):
                self.A[i][j] = self.A[i][j] + other.A[i][j]
            result = self.A
        return Matrix(result)


mtr1 = Matrix([[1, 0, 1], [0, 1, 0]])
mtr2 = Matrix([[0, 1, 0], [1, 0, 1]])
print(mtr1 + mtr2)
...



# задание 2
print('задание_2: суммарный расход ткани')

class Tissue:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def get_tissue_coat(self):
        return self.V / 6.5 + 0.5

    def get_tissue_suit(self):
        return self.H * 2 + 0.3

    @property
    def get_tissue_total(self):
        return str('Всего ткани: ' f'{float((self.V / 6.5 + 0.5) + (self.H * 2 + 0.3))}')


class Coat(Tissue):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.total_c = float(self.V / 6.5 + 0.5)

    def __str__(self):
        return ('Расход ткани на пальто: ' f'{self.total_c}')


class Suit(Tissue):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.total_s = float(self.H * 2 + 0.3)

    def __str__(self):
        return ('Расход ткани на костюм: ' f'{self.total_s}')


tissue = Tissue(1, 2)
print(tissue.get_tissue_total)
coat = Coat(1, 2)
print(coat)
print(coat.get_tissue_total)
suit = Suit(1, 2)
print(suit)
print(suit.get_tissue_total)
...


# задание 3
print('задание_3: клетки')

class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Итого {self.quantity} клеток'

    def __add__(self, other):
        return Cell(int(self.quantity + other.quantity)

    def __sub__(self, other):

        if self.quantity > other.quantity:
            return Cell(int(self.quantity - other.quantity))
        else:
            print (f'Вычитание невозможно, результат < 0')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cell_rows):
        row = ''
        for i in range(int(self.quantity / cell_rows)):
            row += f'{'*' * cell_rows} \n'
        row += f'{'*' * (self.quantity % cell_rows)}'
        return row


cell_1 = Cell(10)
cell_2 = Cell(5)
print((cell_1) + (cell_2))
print(cell_1.make_order(5))
print(cell_2.make_order(2))



