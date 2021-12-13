# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

a = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]
b = [[8, 7, 6, 5], [7, 6, 5, 8], [6, 5, 8, 7], [5, 8, 7, 6]]

class Matrix:
    def __init__ (self, lists):
        self.lists = lists

    def __str__ (self):
        return '\n'.join(map (str, self.lists))

    def __add__ (self, other):
        c = []
        for i in range (len (self.lists)):
            c.append ([])
            for j in range (len (self.lists [(0)])):
                c [i]. append (self.lists [i] [j] + other.lists [i] [j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix (a)
matrix_2 = Matrix (b)

print (matrix_1, '\n')
print (matrix_2, '\n')
print (matrix_1 + matrix_2)