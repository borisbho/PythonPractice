for i in range(5):
    print(i)

print()

for i in range(5,10):
    print(i)

print()

for i in range(0,10,2):
    print(i)

print()

for i in reversed(range(5)):
    print(i)

print()

monsters = ['ghost','vampire', 'werewolf', 'zombie']
for monster in monsters:
    print(monster)

for idx, monster in enumerate(monsters):
    print(idx,monster)

harry = {
    "name": "Harry",
    "age": 42,
    "species": "werewolf"    
}

for i in harry.values():
    print(i)

for key, value in harry.items():
    print(key,value)


questions = ['name', 'age', 'species']
answers = ['Bob', 21, 'Zombie']

for question, answer in zip(questions,answers):
    print(f'What is your {question}? My {question} is {answer}.' )

print()

i = 0
while i < 5:
    print(i)
    i += 1