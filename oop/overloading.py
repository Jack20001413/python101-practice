class Employee:

    # By using optional parameters (var=None) and default value, you can achieve construct overloading in Python.
    # By default, Python does not support calling multiple constructors
    def __init__(self, name, position=None) -> None:
        self.name = name
        self.position = position

    def introduce(self):
        print(f"Hi I'm {self.name}. I'm working as {"an intern" if self.position == None else "a " + self.position.lower()}.")

employee1 = Employee("Lisa")
employee1.introduce()

employee2 = Employee("Annie", "Manager")
employee2.introduce()