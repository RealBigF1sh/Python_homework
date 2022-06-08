file_1 = open('open_me.txt', 'r', encoding='utf-8')
task_list = []
for line in file_1:
    ask = line.split()
    ask_tuple = (ask[0], ask[5], ask[6])
    task_list.append(ask_tuple)
print(task_list)
file_1.close()
