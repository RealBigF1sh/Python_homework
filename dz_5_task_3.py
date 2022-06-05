from itertools import zip_longest
tutors = ['Иван', 'Мария', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Василий', 'Константин']
klasses = ['9A', '8B', '9Б', '8Б', '7А', '9В']
my_gen = (data for data in zip_longest(tutors, klasses, fillvalue=None))
for i in my_gen:
    print(i)
