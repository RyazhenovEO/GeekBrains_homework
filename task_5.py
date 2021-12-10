# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__ (self, title = "Это можно отсортировать."):
        self.title = title

    def draw (self):
        print (f"Начинаем сортировку.")

class Pen (Stationery):
    def draw (self):
        print (f"Начинаем сортировку ручек. {self.title}")

class Pencil (Stationery):
    def draw (self):
        print (f"Начинаем сортировку карандашей. {self.title}")

class Handle (Stationery):
    def draw (self):
        print (f"Начинаем сортировку маркеров. {self.title}")
