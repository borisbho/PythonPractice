import csv

with open('monster.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

writer.writerow(['Bob', 21, 'zombie'])
writer.writerow(['Suzette', 34, 'vampire'])
writer.writerow(['Harry', 42, 'werewolf'])


with open('monster2.csv', mode='w', newline='') as csv_file:
    fields=['name','age','species']
    writer = csv.DictWriter(csv_file,fieldnames= fields)

    writer.writeheader()
    writer.writerow({
        'name' : 'Bob',
        'age' : 21,
        'species' : 'zombie'
    })
    
    writer.writeheader()
    writer.writerow({
        'name' : 'fuckyou',
        'age' : 25,
        'species' : 'bitch'
    })

with open('monster.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    my_list = []
    for indx, row in enumerate(csv_reader):
        print(idx,row)
        my_list.append(row)
    print(my_list)

with open('monsters2.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    my_list.clear()
    for row in csv_reader:
        print(row)
        my_list.append(row)
        print(csv_reader)
        print(my_list)
        print(my_list[1]['name'])