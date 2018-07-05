# srot alg
def search(L, e):
    for i in L:
        if i == e:
            return True
    return False

def binarySearch(L, e):
    mid = len(L) // 2
    if len(L) == 0:
        return False
    elif L[mid] == e:
        return True
    elif e < L[mid]:
        return binarySearch(L[:mid],e)
    elif e > L[mid]:
        return binarySearch(L[mid+1:], e)

print(binarySearch([1,2,3,4,5],2))
print(binarySearch([1,2,3,4,5],1))
print(binarySearch([1,2,3,4,5],3))
print(binarySearch([1,2,3,4,5],4))
print(binarySearch([1,2,3,4,5],5))
print(binarySearch([1,2,3,4,5],6))
print(binarySearch([1,2,3,4,5],0))