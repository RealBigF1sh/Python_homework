import sys
count = sys.argv[1:]
with open('cakes.csv', encoding='utf-8') as c:
    if len(count) == 2:
        start = int(count[0])
        end = int(count[1])
    elif len(count) == 0:
        start = 0
        end = sum(1 for line in c)
        c.seek(0)
    else:
        start = int(count[0])
        end = sum(1 for line in c)
        c.seek(0)

    for idx, line in enumerate(c):
        if start <= idx + 1 <= end:
            print(line.strip)
