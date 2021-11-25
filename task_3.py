# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func (
        number_1 = int (input ('введите первое число: ')),
        number_2 = int (input ('введите второе число: ')),
        number_3 = int (input ('введите третье число: '))
):
    numbers = [number_1, number_2, number_3]
    max_number = max (numbers)
    numbers.remove (max_number)
    sum = max_number + max (numbers)
    return sum

print (my_func ())

