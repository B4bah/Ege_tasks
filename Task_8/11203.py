from itertools import product

words = list(product('РЕКОГНОСЦИРОВКА', repeat=6))
A = []

for i in range(4000, len(words)):
    word = ''.join(words[i]).replace('Е', '1').replace('О', '1').replace('И', '1').replace('А', '1')
    if '1'
    print(word)
    break

print(words[0], type(str(words[0])))