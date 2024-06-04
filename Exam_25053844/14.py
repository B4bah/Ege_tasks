num = 4 * 3125**2019 + 3 * 625**2020 - 2 * 125**2021 + 25**2022 - 4 * 5**2023 - 2024

num_25 = []
while num > 0:
    num_25.append(num % 25)
    num //= 25
    num_25 = num_25[::-1]
print(sum(1 for x in num_25 if x > 10))