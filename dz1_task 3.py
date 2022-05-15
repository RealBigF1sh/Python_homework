for percent in range(0, 100):
    if 11 <= percent <= 14:
        print(percent, 'процентов')
    elif percent % 10 == 1:
        print(percent, 'процент')
    elif 2 <= percent % 10 <= 4:
        print(percent, 'процента')
    else:
        print(percent, 'процентов')
        