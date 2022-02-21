# Из данной строки отобразить только символы нижнего регистра. Использовать библиотеку string.
# Строка 'In PyChapm, you can specify third-party standalone applications and run them as External Tools'.
from string import ascii_lowercase
fraza = 'In PyChapm, you can specify third-party standalone applications and run them as External Tools'
print('все символы нижнего регистра из строки:')
print(*list(filter(lambda x: x in ascii_lowercase, fraza)))