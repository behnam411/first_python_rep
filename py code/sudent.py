class Student:
    def __init__(self, name, degree, grades):
        self.name = name
        self.degree = degree
        self.grades = grades
    def avg(self,student):
        n = 0
        for i in student.grades:
            n += i
        
        print(n/ len(student.grades))