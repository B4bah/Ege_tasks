from itertools import product

words = [word for word in product('01234', repeat=4)]
print(words[210])