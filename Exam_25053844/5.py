def f(n):
    bin_n = f'{n:b}'
    if n % 3 == 0:
        bin_n += bin_n[-2:]
    else:
        bin_n += f'{((n % 3) * 3):b}'
    return int(bin_n, 2)
min_r = 1000000
for num in range(1, 1000):
    R = f(num)
    if R >= 195:
        min_r = min(min_r, R)
print(min_r)