from itertools import product

k = 0
for num in product('0123456', repeat=7):
    if num[0] != '0':
        if sum(1 for x in num if x in '0246') == 2:
            k += 1
print(k)