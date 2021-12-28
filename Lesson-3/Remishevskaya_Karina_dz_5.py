nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

x = int(input('Введите количество шуток: '))

import random


def get_jokes(x):
    joke = []
    while x > 0:
        x -= 1
        joke.append(f'{nouns[random.randint(0, len(nouns)-1)]} {adverbs[random.randint(0, len(adverbs)-1)]} {adjectives[random.randint(0, len(adjectives)-1)]}')
    return joke


print(get_jokes(x))

