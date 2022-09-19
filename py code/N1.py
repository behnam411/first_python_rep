
from pickle import NONE
from re import M

class my_list:
    def __init__(self,tedad=1) :
        self.my_list = [None] * tedad
    
    def __repr__(self) :
        return str(self.my_list)
    
    def __setitem__ (self,index,value):
        self.my_list[index] = value
        
    def __getitem__ (self,index):
        return self.my_list[index]
    def __delitem__(self,index):
        self.my_list[index] = None
        
a = my_list(4)
#a.set_item(0,'in khare k inja neshaste')
#a.set_item(1,'kheyli khare')
#a.del_item(3)
#print(a)
a[0]= 'mamad'
a[1]= 'melody'
del a[1]
print(a)
#class A :
    #def __init__(self,name=None,age=None):
    #    self.name = name
    #    self.age = age
    #def __bool__(self):
    #    return bool(self.age) 
      
#a1 = A('alireza')

#if a1:
#    print('its ok') 
#else:
#    print('sik')   