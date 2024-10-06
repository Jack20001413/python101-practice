# @property - A decorator used to make a method into a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write or delete attributes
#             Gives you setter, getter and deleter method instead of writing getter and setter methods like other programming language

class Employee:

    def __init__(self, name, position) -> None:
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    @name.setter
    def name(self, new_name):
        if new_name == None:
            print("Name must not be empty!")
        else:
            self._name = new_name

    @position.setter
    def position(self, new_position):
        if new_position == None:
            print("Position must not be empty!")
        else:
            self._position = new_position

    @name.deleter
    def name(self):
        del self._name
        print("Name has been deleted!")

    @position.deleter
    def position(self):
        del self._position
        print("Position has been deleted!")


employee = Employee("Kevin", "Manager")

employee.name = "Mavin"
employee.position = "CEO"

print(employee.name)
print(employee.position)

del employee.name
del employee.position