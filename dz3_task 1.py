numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'

}


def num_translate(choice):
    """Translate numbers from english to russian"""
    for key in numbers:
        if key == choice:
            print('Перевод: ', numbers.get(key))


num_translate(input('Введите число на английском: '))
