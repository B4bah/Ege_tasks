with open('26(2)-31-05-2024.txt') as f:
    n, k = map(int, f.readline().split())
    A = [int(x) for x in f.readlines()]
    A = sorted(A)[-2*k:]
    print(A)
    print(int(sum(A[:k])/len(A[:k])), int(sum(A[-k:])/len(A[-k:])))