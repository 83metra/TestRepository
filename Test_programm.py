print('Hallo, world')

def word_construct(obj):
    print(obj)
    if isinstance(obj, list):
        index=int(input('Введите порядковый номер в списке:'))
        word = obj[index - 1]
        return word
    elif isinstance(obj, (str, int)):
        return obj

my_list = ['Мост', 'Ветвь', 'Синица', 'Дом']

print(word_construct(my_list))
