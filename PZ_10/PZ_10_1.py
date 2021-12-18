# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
#   Исходные данные:
#   Количество элементов:
#   Индекс последнего максимального элемента:
#   Меняем местами первую и последнюю трети:
from random import randint

with open('sequence.txt', 'w', encoding='utf-8') as seq:
    for i in range(24):
        k = randint(-100, 100)
        while k == 0:  # избегаю случай появления нуля в последовательности
            k = randint(-100, 100)
        print(k, end=' ', file=seq)  # записываю в файл последовательность

with open('sequence.txt', 'r') as inf:
    line = list(map(int, inf.readline().split()))  # заношу последовательность из файла в список
    max_index = line.index(max(line))
    first_third, second_third, third_third = [], [], []
    k = 0
    for i in line:  # разбиваю изначальную последовательность на трети и заношу каждую в отдельный список
        if k < len(line) / 3:
            first_third.append(i)
            k += 1
        elif len(line) / 3 <= k < (len(line) / 3) * 2:
            second_third.append(i)
            k += 1
        else:
            third_third.append(i)
    print(first_third, second_third, third_third)
    with open('result.txt', 'w', encoding='utf-8') as res:
        print('Исходные данные:', *line, file=res)
        print('Количество элементов:', len(line), file=res)
        print('Индекс максимального элемента:', max_index, file=res)
        print('Меняем местами первую и последнюю трети:', *third_third, *second_third, *first_third, file=res)
