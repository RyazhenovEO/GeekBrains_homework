# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class StoreMashines:
    def __init__ (self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'модель: ': self.name, 'цена: ': self.price, 'количество: ': self.quantity}

    def __str__ (self):
        return f' {self.name} цена: {self.price} количество: {self.quantity}'

    def reception (self):
        try:
            unit = input (f'введите модель: ')
            unit_p = int (input (f'введите цену: '))
            unit_q = int (input (f'введите количество: '))
            unique = {'модель: ': unit, 'цена: ': unit_p, 'количество: ': unit_q}
            self.my_unit.update (unique)
            self.my_store.append (self.my_unit)
            print (f'список: \n {self.my_store}')
        except:
            return f'ошибка ввода данных'

        print (f'для выхода - Q, для продолжения - Enter')
        q = input (f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append (self.my_store)
            print (f'склад: \n {self.my_store_full}')
            return f'выход'
        else:
            return StoreMashines.reception (self)

class Printer (StoreMashines):
    def to_print (self):
        return f'to print smth {self.numb} times'

class Scanner (StoreMashines):
    def to_scan (self):
        return f'to scan smth {self.numb} times'

class Copier (StoreMashines):
    def to_copier (self):
        return f'to copier smth  {self.numb} times'
