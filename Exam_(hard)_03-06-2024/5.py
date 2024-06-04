def f(n):
    bin_n = f'{n:b}'
    if n % 3 == 0:
        bin_n += bin_n[-3:]
    else:
        bin_n += f'{((n % 3) * 3):b}'
    return int(bin_n, 2)


max_r = 0
for num in range(1, 1000):
    R = f(num)
    if R <= 170:
        max_r = max(max_r, R)

print(max_r)