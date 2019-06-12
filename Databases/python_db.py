import sys, getopt 
import os
people = []
try:
    opts, args = getopt.getopt(sys.argv[1:],sys.argv[0:], "a:l:")    
    if sys.argv[1] == '-a':
        try:
             for i in range(2,len(sys.argv)):
                file = open('data.txt', 'a')
                file.write(sys.argv[i] + '\n')
                file.close()
             print('Content Added')
        except FileNotFoundError:
             print('Nahs')
    elif sys.argv[1] == '-l':
        file = open('data.txt', 'r')
        print(file.read())
        file.close()
    else:
        print('nah')
except getopt.GetoptError:
    print('usage: python_db.py -a <content> -l <list>')
    sys.exit()
  
 
 