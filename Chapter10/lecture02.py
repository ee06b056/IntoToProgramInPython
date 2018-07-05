# sort alg
def selSort(L):
    for i in range(len(L)):
        min = L[i]
        minIndex = i
        for j in range(i+1,len(L)):
            if min > L[j]:
                min = L[j]
                minIndex = j
        if not i == minIndex:
            L[i], L[minIndex] = L[minIndex], L[i] 
    return L

# mert sort
import operator
def merge(left, right, compare = operator.lt):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        left = mergeSort(L[:mid], compare)
        right = mergeSort(L[mid:], compare)
        return merge(left, right, compare)

print(merge([1,3,5], [2,4,8,11]))

print(mergeSort([9,5,7,3,10,6,13,12,9]))
