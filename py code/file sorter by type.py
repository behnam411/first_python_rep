
import os, glob
import datetime

folder = input('enter your folder path: ')
files = glob.glob(folder + '/*')
format_set = set()
dt = datetime.datetime.now().strftime('%A')
for file in files:
    format1 = file.split('.').pop()
    format_set.add(format1)
#print(format_set)
def make_dir():
    for format_f in format_set:
        try:
            os.makedirs(folder + '/' + dt + '/' + format_f)
        except:
            continue

def move_file():
    for file in files:
        try:
            format1 = file.split('.').pop()
            from1 = file
            to1 = folder + "/" + dt + '/' + format1 + '/' + file.split('\\').pop()
            #print(file)
            #print(format1)
            #print(folder)
            #print(file.split('\\').pop())
            #print(from1)
            #print(to1)
            os.rename(from1,to1)
        except:
            continue
make_dir()
move_file()