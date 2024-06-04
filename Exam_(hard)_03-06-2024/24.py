with open('24_11813.txt') as f:
    S = f.readline()
    for x in 'EIOU':
        S = S.replace(x, 'A')
    for y in 'CDFGHJKLMNPQRSTVWXZ':
        S = S.replace(y, 'B')
    print(S[:100])

    M = [1] * len(S)
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            M[i] += M[i-1]
    print(max(M))