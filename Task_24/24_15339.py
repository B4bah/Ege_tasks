with open('24_15339.txt') as f:
    s = f.readline().strip().replace('B', 'A').replace('C', 'A').replace('7', '6').replace('8', '6').replace('9', '6')

    while 'AA' in s:
        s = s.replace('AA', 'A A')
    while '66' in s:
        s = s.replace('66', '6 6')
    print(max(len(x) for x in s.split()))