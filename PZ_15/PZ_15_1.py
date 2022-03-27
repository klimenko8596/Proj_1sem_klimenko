# В матрице элементы второго столбца заменить элементами из одномерного
# динамического массива соответствующей размерности.
from random import randint

rows = randint(2, 6)
columns = randint(2, 6)

matrix = []
for i in range(rows):
    my_list = []
    for j in range(columns):  # создание матрицы
        my_list.append(randint(-5, 5))
    matrix.append(my_list)

my_list2 = []
for k in range(rows):
    my_list2.append(randint(-10, 10))  # создание динамического массива соответствующей размерности

print('Изначальная матрица:')
for i in matrix:
    print(i)

print('Изначальный одномерный массив: ', my_list2)
print('Измененная матрица:')
for i in range(rows):
    for j in range(columns):
        if j == 1:
            matrix[i][j] = my_list2[i]  # замена элемента второго столбца матрицы на элемент динамического массива
        print(matrix[i][j], end=' ')
    print()
