def findAvEven(l):
    try:
        for i in l:
            if i % 2 == 0:
                return i
        raise ValueError('No even number')
    except ValueError:
        print('err')

print(findAvEven([1,3,5,7]))