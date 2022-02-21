# Даны две последовательности. Найти элементы, общие для двух последовательностей и их количество.
from random import randint

list_1 = [randint(-100, 100) for i in range(12)]
list_2 = [randint(-100, 100) for j in range(12)]

common = [x for x in list_1 if x in list_2]  # проверка на наличие каждого элемента первого списка во втором списке и
# если это так, занесение его в список
print("Последовательность 1:", *list_1)
print("Последовательность 2:", *list_2)
print("Общие элементы:", *common, "\nИх количество: ", len(common)) if len(common) > 0 else print("Общих элементов нет")
