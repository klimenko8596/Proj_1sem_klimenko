# Вычислить количество отрицательных чисел в наборе
from random import randint
my_list = [randint(-15, 15) for i in range(10)]


def sum_neg(arr, size, count=0):
    if size == 0:
        return count
    else:
        if arr[size - 1] < 0:
            return sum_neg(arr, size - 1, count=count+1)
        else:
            return sum_neg(arr, size-1, count=count)


print(my_list)
print(sum_neg(my_list, len(my_list)))