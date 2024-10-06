class Animal:

    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        print(f"{self.name} is speaking!")

class Cat(Animal):

    # This method overrides parent speak() method
    def speak(self):
        print("Meow!")

cat = Cat("Garfield")
cat.speak()