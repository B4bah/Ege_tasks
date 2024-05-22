num = 3 * 5103 ** 2020 + 3 * 729 ** 2021 - 2 * 343 ** 2022 + 27 ** 2023 - 4 * 7 ** 2024 - 2029


def base36(num):
    d = []
    while num > 0:
        d.append(num % 36)
        num //= 36
    return d


num_36 = base36(num)
print(len([x for x in num_36 if x > 12]))