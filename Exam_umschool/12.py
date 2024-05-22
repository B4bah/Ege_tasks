s = '4' * 65

while '2222' in s or '4444' in s:
    if '2222' in s:
        s = s.replace('2222', '44')
    if '4444' in s:
        s = s.replace('4444', '22')

print(s)