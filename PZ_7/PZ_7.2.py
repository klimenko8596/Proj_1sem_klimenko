# Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов (путь),
# собственно имя и расширение. Выделить из этой строки имя файла (без расширения)

from os import path
full_name = path.basename(r'C:/Users/Пользователь/Desktop/pz_3semestr/pz_7.1.py ')
name = path.splitext(full_name)[0]
print(name)
