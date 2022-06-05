src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [data for data in src if data > src[src.index(data) - 1] and src.index(data) != 0]
print(result)
