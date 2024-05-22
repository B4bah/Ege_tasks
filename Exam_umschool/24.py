with open('24.txt') as f:
    s = f.readline().replace('B', 'A').replace('C', 'A').replace('7', '6').replace('8', '6').replace('9', '6')\
        .replace('AA', '.').replace('66', '.')
    s_ = s.split('.')
    d = [len(x) for x in s_]
    print(max(d)+2)