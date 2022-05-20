prices = [47.51, 92.42, 115, 210.06, 88.11, 71.35, 27.4, 35.5, 67.08, 82.72]

# пункт А
money = []
for num in prices:
    a = int(num)
    b = int(num * 100 % 100)
    num = f'{a} руб {b:02d} коп'
    money.append(num)
delta = ', '.join(money)
print('Список в строке: ', delta)

# пункт B
print('Cписок до сортировки по возрастанию: ', id(prices), prices)
prices.sort()
print('Список после сортировки по возрастанию:', id(prices), prices)

# пункт С
prices.reverse()
print('Список после сортировки по убыванию: ', prices)

# пункт D
print('Пять самых дорогих товаров:', prices[:5])
