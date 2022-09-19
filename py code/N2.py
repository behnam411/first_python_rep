
# class jobs:
    
#     def __init__(self,name,job):
#         self.name = name
#         self.job = job
#     def __contains__(self,item):
#         if item in self.job:
#             return True
        
# a1 = jobs('ali' , 'mandes')
# setattr(a1,'city','tehran')

# print(getattr(a1,'city'))

from ast import arg



def show(name,*args,**kwargs):
    print(f'hello{name}')
    print(args)
    print(kwargs)
    
show('mamad','ali',age=23,height=180)