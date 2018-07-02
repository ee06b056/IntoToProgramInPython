import datetime

class Person(object):
    
    def __init__(self, name):
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def setBirthday(self, birthday):
        self.birthday = birthday

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __str__(self):
        return self.name

class MITPerson(Person):
    nextIdNum = 0

    def __init__(self,name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        Student.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    
class Grad(Student):
    pass

class TransferStudent(Student):
    def __init__(self, name, fromSchool):
        Student.__init__(self, name)
        self.fromSchool = fromSchool

    def getOldSchool(self):
        return self.fromSchool

class Grades(object):
    def __init__(self):
        self.students = []
        



p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
print(p5)
print(type(p5)==Grad)
print(p6, type(p6) == UG)

print(UG)



me = Person('Michale Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')

print(him.getLastName())

him.setBirthday(datetime.date(1961,8,4))
her.setBirthday(datetime.date(1958, 8, 16))

p1 = MITPerson('Barbara Beaver')
print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))