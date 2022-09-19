class oskol:
    def __init__(self,name,age,gender,zeyd):
        self.name = name
        self.age = age
        self.gender = gender
        self.zeyd = zeyd
    def sagi(self):
        if self.zeyd == True:
            return 'sag tu ruhesh'
            
        else :
            return 'az khodemune
        '
            
        
a = oskol('mamad', 24 ,'M',True)

print(a.sagi())
        