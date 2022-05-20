my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
your_list = []
for idx in my_list:
    if idx.isdigit():
        your_list.extend(['"', f'{int(idx):02}', '"'])
    elif (idx.startswith('+') or idx.startswith('-')) and idx[1:].isdigit():
        your_list.extend(['"', f'{idx[0]}{int(idx[1:]):02}', '"'])
    else:
        your_list.append(idx)
delta = ' '.join(your_list)
print('Список в строке: ', delta)
