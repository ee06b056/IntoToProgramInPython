# Hash Map
class intDict(object):
    """Map with key as integer"""
    def __init__(self, numBuckets):
        """create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
    
    def addEntry(self, dictKey, dictVal):
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))

    def getValue(self, dictKey):
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'

import random

D = intDict(29)
for i in range(20):
    key = random.randint(0, 10**5)
    print (key)
    D.addEntry(key, i)
print('The value of the inDict is:')
print(D)
print('\n','The Buckets are:')
for hashBucket in D.buckets:
    print ('    ' , hashBucket)
