# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

def write_numbers (file_path):

    count = random.randint (1, 9)
    try:
        with open (file_path, 'w') as f:
            for _ in range (count):
                f.write (' '.join ( [str (x) for x in random.sample (range (1, 9), random.randint (1, 9))]))
                f.write ('\n')
    except Exception as err:
        print ('Unexpected error:', err)


def calc_numbers (file_path):

    total = 0
    try:
        with open (file_path, 'r') as f:
            for line in f:
                try:
                    total += sum ([float (x) for x in line.split ()])
                except ValueError as err:
                    print ('warning:', err)
    except Exception as err:
        print ('Unexpected error:', err)
    return total


if __name__ == '__main__':
    file_name = 'task5_output_file.txt'
    write_numbers (file_name)
    print ('Total count:', calc_numbers (file_name))