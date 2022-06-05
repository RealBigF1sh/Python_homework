def odd_to(num):
    for data in range(1, num + 1, 2):
        yield data


odd_to_num = odd_to(15)
for k in odd_to_num:
    print(k)
