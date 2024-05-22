with open('26.txt') as f:
    n = int(f.readline())
    # A = sorted([[int(x) for x in row.split()] for row in f.readlines()])
    # n = 4
    # A = sorted([[3, 7], [6, 8], [1, 9], [5, 6]])
    # P = [0] * (max(y[1] for y in A) + 1)
    # for tb in A:
    #     P[tb[0]] += 1
    #     P[tb[1]] -= 1
    # print(P)
    arr_time = [0] * (5 * 10 ** 6)
    for i in range(n):
        st, end = map(int, f.readline().split())
        arr_time[st] += 1
        arr_time[end] -= 1

    pref_arr = [0] * len(arr_time)
    pref_arr[0] = arr_time[0]
    for i in range(1, len(arr_time)):
        pref_arr[i] = pref_arr[i - 1] + arr_time[i]

    mx_odn = max(pref_arr)

    k = 0
    mx_k = 0
    for i in pref_arr:
        if i == mx_odn:
            k += 1
            mx_k = max(k, mx_k)
        else:
            k = 0

    print(mx_odn, mx_k)
