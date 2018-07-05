# O(log(n))
def intTostr(i):
    digits = '0123456789'
    result = ''
    if i == 0:
        return '0'
    while i > 0:
        result += digits[i%10]
        i = i // 10
    return result

# O(n)
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val

def factorial(x):
    if x ==1:
        return 1
    else:
        return x*factorial(x-1)

# polynomial complexity
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

def intersect(L1, L2):
    temp = []
    for e1 in L1:
        if e1 in L2 and e1 not in temp:
            temp.append(e1)
    return temp

# exponential complexity
def getBinaryRep(n, numDigits):
    symbols = '01'
    result = ''
    while numDigits > 0:
        result = symbols[n%2] + result
        n = n // 2
        numDigits -= 1
    if not n == 0:
        raise ValueError('not enough digits')
    return result

def genPowerset(L):
    powerSet = []
    for i in range(2**len(L)):
        subSet = []
        binaryI = getBinaryRep(i, len(L))
        for j in range(len(L)):
            if binaryI[j] == '1':
                subSet.append(L[j])
        powerSet.append(subSet)
    return powerSet

print(genPowerset([1,2,3]))