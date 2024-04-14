from School_homeworks.Funcs.divisors_func import divs

for index, num in enumerate(range(245_690, 245_756)):
    if len(divs(num)) == 2: # Проверка количества делителей числа
        print(index+1, num)
