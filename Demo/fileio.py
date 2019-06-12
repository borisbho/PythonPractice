file = open('text.txt', 'w')
file.write('Hello\n')
file.close()

file = open('text.txt', 'a')
file.write('World!\n')
file.close()

file = open('text.txt', 'a')
file.write('World!\n')
file.close()

file = open('text.txt', 'a')
file.write('World!\n')
file.close()

file = open('text.txt', 'r')
print(file.read())
file.close()

#file = open('text.txt', 'r')
#print(file.read(4))
#file.close()

