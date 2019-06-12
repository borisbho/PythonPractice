monsters1 = ['vampire', 'zombie', 'ghost']
monsters2 = ['vampire', 'zombie', 'ghost']
monsters3 = ['vampire', 'zombie', 'werewolf']

if monsters1 == monsters2:
    print('Yay, monsters1 and monsters2 are equal!')

print(monsters1 == monsters3)

bool1 = True
bool2 = False
print(bool1)
print(not bool1)
print(not bool1 == bool2)
print()

print(isinstance(7, int))
print(isinstance(7.0, float))
print(isinstance('Zombie', str))
print(isinstance(bool1, bool))
print(isinstance('Zombie', int))
print()

if bool1 and bool2 is False:
    print('Both of these are true')

if bool1 or bool2:
    print('At least one of these is true')

if bool1 == bool2:
    print('Really?')
else:
    print("That's what I thought.")

a=2
if a == 1:
    print('Not likely')
elif a == 2:
    print('That makes sense')