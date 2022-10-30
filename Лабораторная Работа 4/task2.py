def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower().split()
    str_ = "".join(str_)
    for i in range(0, len(str_)):
        if str_.isalpha==False:
            str_.replace(str_[i], "")
    c = dict()
    for letter in str_:
        c[letter] = c.get(letter, 0) + 1
    return c

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
