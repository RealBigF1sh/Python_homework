import json
from itertools import zip_longest
dict_combine = {}
with open('names.csv', encoding='utf-8') as file_names, open('hobbies.csv', encoding='utf-8') as file_hobbies:
    countlines_names = sum(1 for line in file_names)
    countlines_hobbies = sum(1 for line_1 in file_hobbies)

    if countlines_names < countlines_hobbies:
        exit(1)

    file_names.seek(0)
    file_hobbies.seek(0)
    for line_names, line_hobbies in zip_longest(file_names, file_hobbies):
        dict_combine[line_names.strip()] = line_hobbies.strip() if line_hobbies is not None else line_hobbies

with open('task_3.json', 'w', encoding='utf-8') as f:
    json.dump(dict_combine, f, ensure_ascii=False)
print(dict_combine)
