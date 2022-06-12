import os

pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for main, folders in pattern.items():
    if os.path.exists(main):
        print(main, 'существует')
    else:
        for folder in folders:
            cur_dir = os.path.join(main, folder)
            os.makedirs(cur_dir)
            