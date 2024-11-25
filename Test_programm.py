print('Hallo, world!')

def word_construct(obj):
    print(obj)
    if isinstance(obj, (list, tuple)):
        index=int(input('Введите порядковый номер в списке:'))
        while index > len(obj) or index < 1:
            index = int(input('Индекс больше длины списка или отрицательный! Введите ещё раз порядковый номер в списке:'))
        word = obj[index - 1]
        return word
    elif isinstance(obj, (str, int)):
        return obj
    else:
        return obj

my_list = ['Мост', 'Ветвь', 'Синица', 'Дом']
my_str = 'Абра-Кадабра'
my_int = 45

new_string = 'Это строка из варианта-1!'

# print(word_construct(my_list))
# print(my_int)
print(my_str)
print(new_string)