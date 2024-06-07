with open('24_934.txt') as f:
    s = f.readline()
    s = 'AFJDKSFJFDCCDBBBACDDDDFFF'
    M = [1] * len(s)
    for i in range(1, len(s)):
        if s[i] >= s[i-1]:
            M[i] += M[i-1]

    D = sorted(M)[::-1]
    B = []
    for n in D:
        B.append(s[M.index(n) - n+1:M.index(n)+1])
    for x in B:
        x_ = {b for b in x}
        if len(x_) == 3:
            print(len(x), x)


    # print(s[M.index(max(M)) - max(M)+1:M.index(max(M))+1])