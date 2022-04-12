translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
             'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
             'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
num = input('Введите число: ')


def num_tranlate(x):
    return translate.get(x)


print(num_tranlate(num))
