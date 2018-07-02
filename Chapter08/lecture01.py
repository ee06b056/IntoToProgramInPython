class IntSet(object):
    def __init__(self):
        print('init construct function')
        self.vals = []

    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    
    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+' not found')

    def getMember(self):
        return self.vals[:]

    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e)+','
        return '{'+result[:-1]+'}'
    
s = IntSet()
s.insert(s,1)
s.insert(s,12)
# s.insert(3)
# s.insert(14)
s.insert = IntSet.remove
print(s)
s.insert(s, e = 1)
print(s)
