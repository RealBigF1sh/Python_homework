import os
my_files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        my_files.append(os.stat(file_path).st_size)
max_size = max(my_files)
i = 1
out_dict = {}
for one in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0
for file in my_files:
    out_dict[10 ** len(str(file))] += 1
print(out_dict)
