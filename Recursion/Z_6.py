# Возведение числа x в степень y
def my_namb(x, y):
    return 1 if y == 0 else x * pow(x, y-1)


print(my_namb(2, 4))