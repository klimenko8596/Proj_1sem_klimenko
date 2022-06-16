# Рекурсивная функция - возвращает ряд Фибоначчи в виде списка.
# Параметр n - максимальное значение в списке.
def fibon_list(n):
    global my_list
    if n != 0:
        my_list.append(my_list[-1] + my_list[-2])
        fibon_list(n - 1)
    return my_list


my_list = [1, 2]
print(fibon_list(15))