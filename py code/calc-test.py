
from sudent import Student

student1 = Student('mamad', 'mandesi', [12,14,16,20],13)

#print(student1.grades)

def avg(student1):
        n = 0
        for i in student1.grades:
            n += i
        
        print(n/ len(student1.grades))
        
print(student1.avg)