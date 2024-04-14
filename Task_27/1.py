k = 2
n = 6
A = [5, 7, 3, 1, 3, 9]

A_ = sorted(A)[::-1]
B = {A[i]: A_.index(A[i]) - A_.index(A[i+1]) for i in range(len(A)-1)}
print(A)
print(A_)
print(B)