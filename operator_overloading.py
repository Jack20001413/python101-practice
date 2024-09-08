'''
Operator overloading is used in a class to change the default behavior of some operations (+, -, /,.etc)
'''

class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    '''This is changing the 'greater than' operation by comparing 2 objects' age'''
    def __gt__(self, other):
        return True if self.age > other.age else False

roger = Dog('Roger', 8)
syd = Dog('Syd', 9)

print(roger > syd)