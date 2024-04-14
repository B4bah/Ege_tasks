from fnmatch import fnmatch
from School_homeworks.Funcs.divisors_func import divs

for num in range(2, 10**7+1):
    if fnmatch(str(num), '3?1111*'):
        if len(divs(num)) == 2:
            print(num)