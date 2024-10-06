from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def speak(self):
        return "Woof!"

dog = Dog("Sparky")
print(dog.speak())