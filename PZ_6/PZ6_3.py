# Практическая №6 №3
# Дано множество A из N точек на плоскости и точка B (точки заданы своими координатами x, y). Найти точку из множества
# A, наиболее близкую к точке B. Расстояние R между точками с координатами (x1, y1) и (x2, y2) вычисляется по формуле:
# R = sqrt((x2 - x1)**2 + (y2 - y1)**2). Для хранения данных о каждом наборе точек следует использовать по два списка:
# список для хранения абсцисс, второй - для хранения ординат.
import math  # Вызов математической библиотеки для дальнеших расчётов
from random import choices  # Вызов рандома для генерации координат

print('Введите количество точек в множестве A')  # Информируем, что нужно ввести пользователю
N = int(input())  # Ввод количества координат в множестве A
r = range(100)  # Максимальное значение координаты
A = []  # Создаём пустой список для множеста координат
B = []  # Создаём пустой список для одной координаты
for i in range(N):  # Делаем цикл для создания рандомных значений в количестве N
    x, y = choices(r, k=2)  # Создание рандомной координаты, каждый круг
    A.append((x, y))  # Каждую рандомную координату заводим в список в виде кортежа
print('Множество точек A:', A)  # Выводим рандомное множество точек A
x, y = choices(r, k=2)  # Создаём рандомнуб координату
B.append(x)  # Добавляем x координата в лист B
B.append(y)  # Добавляем y координата в лист B
print('Точка B:', B)  # Выводим рандомную точку B
# Расчитываем разницу координат и выводим координату с минимальной разницой
print('Самая близкая точка из A к точке B', (min(A, key=lambda point: math.hypot(B[1] - point[1], B[0] - point[0]))))
