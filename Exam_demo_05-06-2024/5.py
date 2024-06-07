def f(n):
    bin_n = f'{n:b}'
    if n % 3 == 0:
        bin_n += bin_n[-3:]
    else:
        bin_n += f'{((n % 3) * 3):b}'
    return int(bin_n, 2)


min_r = 10000
for num in range(1, 1000):
    if f(num) > 151:
        min_r = min(min_r, f(num))
print(min_r)