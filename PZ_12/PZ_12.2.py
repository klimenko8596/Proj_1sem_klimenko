# Дано целое число N (> 0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N
from tkinter import *
from tkinter import messagebox, ttk


def show_solution():
    n = N.get()
    try:
        n = int(n)
        if n <= 0:
            messagebox.showinfo('Нахождение суммы по формуле.', 'Число не положительное!') # обработка исключений
    except ValueError:
        messagebox.showinfo('Нахождение суммы по формуле.', 'Неправильно ввели целое число!')
    if type(n) == int and n > 0:
        a = 0
        for i in range(1, n + 1): # проведение расчетов
            a += 1/i
        messagebox.showinfo('Нахождение суммы по формуле.', f'Сумма равна: {a}')


root = Tk()
root.title('Нахождение суммы по формуле.')
root.geometry("580x130+350+350")
root.resizable(width=False, height=False)

N = StringVar()

Label(text='Нахождение суммы по формуле: 1 + 1/2 + 1/3 + ... + 1/n', font='Arial 15').place(x=5, y=2)
Label(text='Введите N:', font='Arial 15').place(x=5, y=40)
myEntry = ttk.Entry(width=15, textvariable=N)
myEntry.place(x=120, y=45)

button = ttk.Button(text='Решить', command=show_solution, width=8)
button.place(x=20, y=85)

root.mainloop()
