# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__ (self, lenght, width, weight, thickness):
        self.lenght = lenght
        self.width = width
        self.weight = weight
        self.thickness = thickness

    def result (self):
        return f"Масса асфальта = {self.lenght} * {self.width} * {self.weight} * {self.thickness} = " \
               f"{(self.lenght * self.width * self.weight * self.thickness) / 1000} т."

road = Road (20, 5000, 25, 5)
print (road.result ())