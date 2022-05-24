import random

nouns = ['автомобиль', 'лес', 'козёл', 'столб', 'огонь']
adverbs = ['утром', 'сегодня', 'завтра', 'вечером', 'позавчера']
adjectives = ['сухой', 'весёлый', 'яркий', 'влажный', 'толстый']


def get_jokes(ask):
    """Pick up words from 3 lists to create a joke"""
    jokes = []
    for i in range(ask):
        jokes.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return jokes


question = (int(input('Введите любое число: ')))
print(get_jokes(question))
