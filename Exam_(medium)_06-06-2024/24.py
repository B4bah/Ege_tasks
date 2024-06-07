with open('24_1040.txt') as f:
    s = f.readline()
    for y in '123456789':
        s = s.replace(y, '0')
    print(s[:100])

    M = [0] * len(s)
    M[0] = int(s[0] == '0')
    for i in range(1, len(s)):
        if s[i] == '0':
            M[i] = M[i-1]+1
    print(max(M))