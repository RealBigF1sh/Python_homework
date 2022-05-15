list_j = []
triple = [index ** 3 for index in range(1, 1000, 2)]
for number in triple:
    a = number % 10
    b = number // 10
    c = b % 10
    d = b // 10
    e = d % 10
    f = d // 10
    g = f % 10
    h = f // 10
    i = h % 10
    j = h // 10
    k = j % 10
    l = j // 10
    m = l % 10
    n = l // 10
    o = n % 10
    p = n // 10
    q = p % 10
    r = p // 10
    result = a + c + e + g + i + k + m + o + q
    if result % 7 == 0:
        list_j.append(number)
print('Сумма чисел 1 списка равна: ', sum(list_j))
list_k = []
for number_one in triple:
    number_one = number_one + 17
    a = number_one % 10
    b = number_one // 10
    c = b % 10
    d = b // 10
    e = d % 10
    f = d // 10
    g = f % 10
    h = f // 10
    i = h % 10
    j = h // 10
    k = j % 10
    l = j // 10
    m = l % 10
    n = l // 10
    o = n % 10
    p = n // 10
    q = p % 10
    r = p // 10
    result = a + c + e + g + i + k + m + o + q
    if result % 7 == 0:
        list_k.append(number_one)
print('Сумма чисел 2 списка равна: ', sum(list_k))
