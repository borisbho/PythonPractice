import sys, getopt
import os
import json
import os.path

def load_json():
    file = open('db.json', 'r')
    people = json.loads(file.read())            
    file.close() 
    return people

def dump_json(p):
    file = open('db.json', 'w')
    file.write(json.dumps(p, indent = 4))
    file.close()

def main(argv):
   try:
        people = []

        if sys.argv[1] == '-a':
            if len(sys.argv) != 6:
                 print('db -a fname lname phone email :adds new record')
                 sys.exit()
            else:
                peoples = {
                    'fname':sys.argv[2],
                    'lname':sys.argv[3],
                    'phone':sys.argv[4],
                    'email':sys.argv[5]
                }
                try:
                    file = open('db.json', 'r')
                    ok = file.read()
                    if ok != '[]' and ok == '':
                        dump_json(people)
                        
                    people = load_json()           
                    people.append(peoples)
                    dump_json(people)
                    print(peoples['fname'] + ' ' + peoples['lname'] + ' ADDED') 
        
                except FileNotFoundError:
                    print('Error: db.json File Not Found')

        elif sys.argv[1] == '-d':
            if len(sys.argv) != 3:
                print(' db -d search :deletes one record')
            else:
                myData = load_json()
                for a in myData:
                    if(a['fname'].lower() == sys.argv[2].lower() or a['lname'].lower() == sys.argv[2].lower() or a['phone'].lower() == sys.argv[2].lower() or a['email'].lower() == sys.argv[2].lower()):
                        print(a['fname'] + ' ' + a['lname'] + ' DELETED')
                        myData.remove(a)
                dump_json(myData)
                                 
        elif sys.argv[1] == '-f':
            if len(sys.argv) != 3:
                print(' db -f search :finds one record')
            else: 
                my_data = load_json()
                for a in my_data:
                    if(a['fname'].lower() == sys.argv[2].lower() or a['lname'].lower() == sys.argv[2].lower() or a['phone'].lower() == sys.argv[2].lower() or a['email'].lower() == sys.argv[2].lower()):
                        print(a['fname'] + '\n' + a['lname'] + '\n' + a['phone'] + '\n' + a['email'])
        
        elif sys.argv[1] == '-l':
            if len(sys.argv) != 2:
                print(' db -l :lists all records')
            else:
                try:
                    file = open('db.json', 'r')
                    my_data = load_json()
                    for a in my_data:
                        print(a['fname'] + '\n' + a['lname'] + '\n' + a['phone'] + '\n' + a['email'])
                        print('------------------------------------------------------')            
                except FileNotFoundError:
                    print('No File')
   except (getopt.GetoptError, IndexError):
    print('usage: python_db2.py -a [fname] [lname] [phone] [email] -f [content] -d [content] -l')
    sys.exit()
if __name__ == "__main__":
   main(sys.argv[1:])
