def tesaurus(*names):
    my_dict = dict()
    for name in names:
        my_dict.setdefault(name[0], [])
        my_dict[name[0]].append(name)
    return my_dict


print(tesaurus("Илья", "Евгений", "Ирина", "Елена", "Владимир"))
