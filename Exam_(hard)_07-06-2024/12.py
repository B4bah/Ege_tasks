from itertools import product

for a in range(1, 50):
    for s_ in product('123', repeat=a):
        s = '0' + ''.join(s_) + '0'
        while not( '00' in s):
            s = s.replace('01', '220', 1)
            s = s.replace('02', '1013', 1)
            s = s.replace('03', '120', 1)
        if s.count('1') == 13 and s.count('2') == 18:
            print(len(s), s)