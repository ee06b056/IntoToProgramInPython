string = input('Input a string: ')
total = 0
substring = ''
for c in string:
    if c == ' ':
        continue
    elif c == ',':
        total = total + float(substring)
        substring = ''
    else:
        substring += c
        print(substring)
total = total + float(substring)
print(total)