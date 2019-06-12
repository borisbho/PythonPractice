import json

bob = '{"name": "Bob","age": 21,"species": "zombie"}'

new_bob = json.loads(bob)
#print(new_bob)

monsters = [
    {
        'name': 'Harry',
        'species': 'Werewolf'
    }
]

file = open('monster.json', 'w')
file.write(json.dumps(monsters))
file.close()

 

file = open('monster.json', 'r')
new_monsters = json.loads(file.read())
file.close()

print(new_monsters)

