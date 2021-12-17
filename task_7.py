# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__ (self, number_1, number_2, *args):
        self.number_1 = number_1
        self.number_2 = number_2
        self.result = 'a + b'

    def __add__ (self, other):
        print (f'Сумма result_1 и result_2 равна')
        return f'result = {self.number_1 + other.number_1} + {self.number_2 + other.number_2}'

    def __mul__ (self, other):
        print (f'Произведение result_1 и result_2 равно')
        return f'result = {self.number_1 * other.number_1 - (self.number_2 * other.number_2)} + {self.number_2 * other.number_1}'

    def __str__ (self):
        return f'result = {self.number_1} + {self.number_2}'
