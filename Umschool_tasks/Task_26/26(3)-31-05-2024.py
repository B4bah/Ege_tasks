with open('26(3)-31-05-2024.txt') as f:
    n, k, m = map(int, f.readline().split())
    A = [int(x) for x in f.readlines()]
    # n, k, m = 10, 2, 4
    # A = [244, 39, 213, 108, 132, 18, 46, 52, 242, 179]
    A = sorted(A)[-(k+m):]
    print(int(sum(A[:m])/len(A[:m])), min(A[-k:]))