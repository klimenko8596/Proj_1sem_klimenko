# реверсирование числа
def rev(n):
    n = str(n)
    return '' if n == '' else n[-1] + rev(n[:-1])


print(rev(12345))