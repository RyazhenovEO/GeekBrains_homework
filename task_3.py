# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class Error:
    def __init__ (self, *args):
        self.list = []

    def input (self):
        while True:
            try:
                element = int (input ('введите число: '))
                self.list.append (element)
                print (f'Список: {self.list} \n')
            except:
                print (f"введено неверное значение")
                choise = input (f'попробовать снова или выйти - Y/N ')

                if choise == 'Y' or choise == 'y':
                    print (try_except.input ())
                elif choise == 'N' or choise == 'n':
                    return f'конец прграммы'
                else:
                    return f'конец программы'
        print (self.list)

try_except = Error (1)
print (try_except.input ())