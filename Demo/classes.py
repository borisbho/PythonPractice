class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.species = 'human'

    def says(self):
        print(self.name + ' says, "Hi, how are you? Nice weather we\'re having."' )
        
sally = Person('Sally', 21)
sally.says()
sally.age = 22
print(sally.age)

class Monster(Person):
    def __init__(self, name, age, species):
        Person.__init__(self, name, age)
        self.species = species

    def says(self):
        print(self.name + ' says, "Grrrr!"')
    

harry = Monster('Harry', 42, 'werewolf')
print(harry.name, harry.age, harry.species)
harry.says()