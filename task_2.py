# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list = []
copy_list = []

counter = int (input ('введите желаемое количество элементов в списке: '))
while len (list) < counter:
    list.append (input ('введите ' + str (len (list) + 1) + '-й элемент списка: '))
    continue
# print (list)

el_1 = 0
el_2 = 1

while el_2 < len (list):
    copy_list.append (list [el_2])
    copy_list.append (list [el_1])
    el_1 += 2
    el_2 += 2
    continue

if len (list) % 2 != 0:
    copy_list.append (list [len (list) - 1])

print (copy_list)