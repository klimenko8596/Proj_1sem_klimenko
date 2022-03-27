# В матрице найти среднее арифметическое положительных элементов, кратных 3.
from random import randint

rows = randint(2, 6)
columns = randint(2, 6)

matrix = []
for i in range(rows):
    my_list = []
    for j in range(columns):  # создание матрицы
        my_list.append(randint(-5, 5))
    matrix.append(my_list)

krat3 = []
print('Матрица:')
for i in matrix:
    for j in i:
        if j > 0 and j % 3 == 0:
            krat3.append(j)
    print(i)

if len(krat3) > 0:
    print('Положительные элементы кратные 3:', *krat3)
    print('Среднее арифметическое этих элементов:', sum(krat3) / len(krat3))
else:
    print('Положительных элементов кратных трем нет')
