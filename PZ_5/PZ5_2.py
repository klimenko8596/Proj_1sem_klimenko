# Практическая №5 №2
# Описать функцию Swap(X, Y), меняющию содержимое переменных X и Y (X и Y - вещественные параметры, являющиеся
# одновременно входными и выходными). С её помощью для данных переменных A, B, C, D  последовательно поменять содержимое
# следующих пар: A и B, C и D, B и C, и вывести новые значения A, B, C, D
def Swap(X, Y):  # Создаём функцию, меняющую содержимое
    X, Y = Y, X 
    return X  # Возвращаем только результат


A, B, C, D = float(input()), float(input()), float(input()), float(input()) 
print(Swap(A, B))  # Используя функцию меняем содержимое пары: A и B и выводим резултат
print(Swap(B, C))  # Используя функцию меняем содержимое пары: B и C и выводим резултат
print(Swap(C, D))  # Используя функцию меняем содержимое пары: C и D и выводим резултат
print(D) 
