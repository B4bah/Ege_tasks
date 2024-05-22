def f(n):
    n_b = f'{n:b}'
    if n % 2 != 0:
        r = '10' + n_b
    else:
        r = '1' + n_b + '10'
    return int(r, 2)


for num in range(1, 1000):
    if f(num) > 697:
        print(num)
        break