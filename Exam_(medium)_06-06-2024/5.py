def f(n):
    bin_n = f'{n:b}'
    if n % 2 == 0:
        bin_n += '01'
    else:
        bin_n += '10'
    return int(bin_n, 2)


min_r = 10000
for num in range(1, 100):
    if f(num) > 81:
        min_r = min(min_r, f(num))
print(min_r)