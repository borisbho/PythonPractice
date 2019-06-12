a = 3
b = 4
print(a + b)

x = a
a = 5
print( a, x )

c = 3.14
d = a + c
e = d - a
print(c, d, e)

a = True
print(a)

my_string = 'ABCDEFGHIJKLM'
print(my_string)
print(len(my_string))
print(my_string[3])

print(my_string[5:10])
print(my_string[2:])
print(my_string[:3])
print(my_string[:-3])

print(my_string[::2])
print(my_string[3:9:2])
print(my_string[::-1])

my_string = my_string*2
print(my_string)
print()

greeting = "Howdy"
name = "Bob"
print(greeting + ', ' + name + "!")
print(f"{greeting}, {name}!")
print("{0}, {1}!".format(greeting, name))
print("Hello, {my_name}!".format(my_name='Sally'))
print("%s, my name is %s." %("Hiya", "Harry"))
print()
print("Hello, my name is %s, and I am %.2f years old" %("Jim", 21))
print("Hello, my name is %s, and I am %.10f years old" %("Jim", 21))
print("Hello, my name is %s, and I am %.20f years old" %("Jim", 21))
print()
email = """
Date: {date}

Dear {name}

I am looking forward to meeting you on the hill.

Sincerely,
{my_name}
"""

import datetime
todaysDate = datetime.date.today()
the_date = '{today.month}/{today.day}/{today.year}'.format(today=todaysDate)
print(the_date)
print(email.format(date=the_date, name='Jill', my_name='Jack'))
print()

num1 = input("Enter the first number-> ")
num2 = input("Enter the second number-> ")
num3 = int(num1) + int(num2)
print(f"{num1} + {num2} = {num3}")