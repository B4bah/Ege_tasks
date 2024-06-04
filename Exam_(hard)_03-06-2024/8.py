from itertools import product

k = 0
for word in product('kkkkee', repeat=4):
    if word[0] == 'k':
        if word[-1] == 'e':
            k += 1

print(k)