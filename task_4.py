# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__ (self, name, color, speed, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go (self):
        print (f"{self.name} поехала")

    def stop (self):
        print(f"{self.name} остановилась")

    def turn (self, direction):
        if direction == 1:
            print (f"{self.name} повернула направо")
        else:
            print(f"{self.name} повернула налево")

    def show_speed (self):
        print (f"Скорость автомобиля {self.name} - {self.speed} км/ч")

class TownCar (Car):
    def show_speed(self):
        if self.speed > 40:
            print (f"Внимание! Автомобиль {self.name} - превысил допустимую скорость")
        else:
            print(f"Скорость автомобиля {self.name} - {self.speed} км/ч")

class WorkCar (Car):
    def __init__ (self, carrying):
        self.carrying = carrying

    def weight (self):
        print (f"Грузоподъемность автомобиля {self.name} - {self.carrying} т")

class SportCar (Car):
    def __init__ (self, second):
        self.second = second

    def time (self):
        print (f"Разгон автомобиля {self.name} от 0 до 100 км/ч - {self.second} с")

class PoliceCar:
    def __init__ (self, speed, color, name, is_police = True):
        police.__init__ (name, color, speed, is_police)
