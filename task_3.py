# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

summa = 0
count = 0
workers = []
with open ("task_3_input_file.txt", "r") as my_file:
    for line in my_file:
        print (line, end="")
        salary = line.split (': ')
        if int (salary [1]) < 20000:
            workers.append (salary [0])
        summa += int(salary [1])
        count += 1
profit = summa / count
print (f"persons: {workers}")
print (f"averate: {profit}")