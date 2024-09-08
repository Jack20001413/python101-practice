class Animal:
    def walk(self):
        print("walking...")

class Dog(Animal):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def bark(self):
        print("woof!")

kiki = Dog("Kiki", 10)

print(type(kiki))
print(kiki.name)
print(kiki.age)
kiki.bark()
kiki.walk()