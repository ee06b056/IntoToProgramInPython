class Grades(object):
    """Mapping relationship from students to grades"""
    def __init__(self):
        """create an empty grades record"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
        
    def getGrades(self, student):
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def getStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
    
# def gradeReport(course):
#     report = ''
#     for s in course.getStudents():
#         tot = 0.0
#         numGrades = 0
#         for g in course.getGrades(s):
#             tot += g
#             numGrades += 1
#         try:
#             average = tot/numGrades
#             report = 

arr1 = [1,2,3,4,5,6,7,8,9]

def test(arr):
    for i in arr:
        print(i)
        yield i

for i in test(arr1):
    print(i)