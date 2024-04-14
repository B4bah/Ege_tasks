string = '1' * 77

while True:
    if '11111' in string:
        string = string.replace('222', '1', 1)
        string = string.replace('111', '2', 1)
    else:
        break
print(string)