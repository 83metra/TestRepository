print('Hallo, world')

def word_construct(obj):
    print(obj)
    if isinstance(obj, list):
        index=int(input('Введите порядковый номер в списке:'))
        while index > len(obj) or index < 1:
            index = int(input('Индекс больше длины списка или отрицательный! Введите ещё раз порядковый номер в списке:'))
        word = obj[index - 1]
        return word
    elif isinstance(obj, (str, int)):
        return obj

my_list = ['Мост', 'Ветвь', 'Синица', 'Дом']

my_int = 45

print(word_construct(my_list))
print(my_int)