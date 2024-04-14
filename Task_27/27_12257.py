def max_sum_subsequence_length(arr, K):
    n = len(arr)

    max_sum = 0
    current_sum = 0
    length = 0

    for i in range(n):
        current_sum += arr[i]

        if current_sum % K == 0:
            max_sum = current_sum
            length = i + 1

    return length


def process_file(file_path):
    with open(file_path, 'r') as file:
        N = int(file.readline().strip())
        heights = [int(file.readline().strip()) for _ in range(N)]

    K = 113
    result = max_sum_subsequence_length(heights, K)

    return result


file_A_path = '27-A_12257.txt'
file_B_path = '27-B_12257.txt'

result_A = process_file(file_A_path)
result_B = process_file(file_B_path)

print(f"Результат для файла A: {result_A}")
print(f"Результат для файла B: {result_B}")
