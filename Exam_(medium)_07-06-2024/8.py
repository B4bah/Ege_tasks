from itertools import product

j = 1
for word in product('КЕГЭ2023', repeat=4):
    j += 1
    if word[0] in '023':
        if all(word[i] != word[i+1] for i in range(3)):
            print(j)
            break