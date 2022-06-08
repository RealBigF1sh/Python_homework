import sys
price = sys.argv[1]
with open('cakes.csv', 'a', encoding='utf-8') as c:
    c.write(price + '\n')
