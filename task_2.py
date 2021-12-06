# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open("task_2_input_file.txt") as my_file:
    for strip in my_file:
        print(strip, end = '')
    size_strips = sum (1 for strip in open("task_2_input_file.txt", "r"))
    print('\n', 'Количество строк в файле - ', size_strips)

    counter = 1
    size_words = [len(word.rstrip().split()) for word in open("task_2_input_file.txt", "r") if word.rstrip()]
    while counter <= size_strips:
        for word in size_words:
            print (f'количество слов в {counter} строке - {word}')
            counter += 1
