# Дано четное число N (> 0) и символы C1 и C2. Вывести строку длины N,
# которая состоит из чередующихся символов C1 и C2, начиная с C1.

N = int(input('введите длину: '))  # длина строки
C1 = input("введите 1 число:")
C2 = input("введите 2 число:")
if N % 2 == 0:  # исключаем, что число может быть нечётным
    print((C1 + C2) * int((N / 2)))
else:
    print('Нечётное число')

if N < 0:  # исключаем, что число меньше нуля
    print("ошибка")
