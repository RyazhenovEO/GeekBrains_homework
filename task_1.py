# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list = ['metrology', 441, ('rostest', 'vibration', 'acoustic'), 84.3]

counter = 0

while counter < len (list):
    element = list [counter]
    print (element, type (element))
    counter += 1


print ('\n')


for element in list:
    print (element, type (element))