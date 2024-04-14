with open('24_15339.txt') as f:
    s = f.readline().strip().replace('B', 'A').replace('C', 'A').replace('7', '6').replace('8', '6').replace('9', '6')
    s_ = s.replace('AA', 'A.').replace('11', '1.')
    a = s_.split('.')
    print(len(max(a)))