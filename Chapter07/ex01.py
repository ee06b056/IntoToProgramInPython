def sumDigits(s):
    try:
        sum = 0
        for i in s:
            if i in '0123456789':
                sum += int(i)
    except Exception:
        print('err')
    return sum
print(sumDigits('bb89jh7hii 8'))