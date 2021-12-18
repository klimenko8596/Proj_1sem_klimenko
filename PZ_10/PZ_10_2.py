# Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку фразой введенной
# пользователем.
with open('text18-9.txt', 'r', encoding='utf-8') as inf:
    chars = inf.read()
    print(chars, end='\n\n')
    k = 0
    for i in chars:
        if i.islower():  # подсчет букв в нижнем регистре
            k += 1
    print('Букв в нижнем регистре:', k)
    with open('result2.txt', 'w', encoding='utf-8') as res:
        j = 0
        m = chars.count('\n')
        for i in chars:  # вывожу стих без последней строчки
            if j == m:
                continue
            if i == '\n':
                j += 1
            print(i, end='', file=res)
        print(input('Введите фразу: '), end=' ', file=res)  # последняя строчка введена пользователем
