from itertools import product

lst = list(map(''.join, product('FROG', repeat=3)))

print(lst.index([x for x in lst if not ('F' in x)][0]))
print(*lst[:25])