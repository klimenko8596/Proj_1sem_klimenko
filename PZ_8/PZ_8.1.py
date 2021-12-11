# Практическая №8
# Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая средние температуры по месяцам в году.
# Преобразовать информацию из строки в словарь, с использованием функции найти среднюю и минимальные температуры,
# результаты вывести на экран.
dano = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'.split(' ')  # Строка с данными, сразу преобразуем её в список
slovar = {dano[0]: dano[1:]}  # Создаём словарь с ключём в виде года и значениями в виде температур
spisok_value_int = []  # Создаём пустой список для дальнейшей работы
for i in dano[1:]:  # Создаём цикл и проходимся по каждому значению, после первого
    spisok_value_int.append(int(i))  # Добавляем в каждом круге целое значение температуры в пустой список
slovar['2020год'] = spisok_value_int  # Присваеваем ключу(году) целочисленный список температур


def temp_avg_min_value():  # Создаём функцию для подсчёта среднего и минимального значений
    print(min(slovar['2020год']))  # Используя 'min' выводим минимальную температуру в 2020
    print(sum(slovar['2020год']) / len(slovar['2020год']))  # Находим среднее значение температур в 2020 и выводим


temp_avg_min_value()  # Вызываем функцию для подсчёта и вывода решения
