with open('24_1_07-06-2024.txt') as f:
    s = f.readline()
    print(s[:10])
    # M = [0] * len(s)
    # M[0] = int(s[0] == 'Y')
    # for i in range(1, len(s)):
    #     if s[i] == 'Y':
    #         M[i] += M[i-1]
    # print(max(M))