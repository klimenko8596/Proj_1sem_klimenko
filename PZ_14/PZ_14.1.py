# В исходном текстовом файле (Dostoevsky.txt) найти все варианты фамилии
# Достоевского (т.е. с различными окончаниями, например, Достоевский,
# Достоевского) в единственном экземпляре.
import re
with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()
reg = re.compile(r'Достоевск\w+', re.M)
familii = re.findall(reg, text)
counter = [familii.count(i) for i in familii]
my_dict = dict(zip(familii, counter))
print('Вывод словаря для проверки: ', end='')
print(*my_dict.items())
print('Фамилия в единственном варианте: ', end='')
for i in my_dict.keys():
    if my_dict[i] ==1:
        print(i)
