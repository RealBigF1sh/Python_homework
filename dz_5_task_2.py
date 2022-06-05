ask = int(input('Введите число: '))
my_gen = (nums for nums in range(1, ask + 1, 2))
for i in my_gen:
    print(i)
