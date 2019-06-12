def hello():
    print('Hello')

hello()

def hi(name):
    print(f'Hi {name}')

hi('Boris')


people = ['Fred', 'Sally', 'Jim', 'Diane']

def greetPeople(greeting, peeps):
    for person in peeps:
        print(f'{greeting}, {person}!')

greetPeople('Hey', people)