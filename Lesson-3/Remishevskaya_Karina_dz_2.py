translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
             'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
             'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
num = input('Введите число: ')


def num_tranlate_adv(num):
    if num[0].isupper():
        num = num.lower()
        return translate[num].capitalize()
    else:
        return translate[num]


print(num_tranlate_adv(num))

