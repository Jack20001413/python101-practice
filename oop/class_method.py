# Class method - Allows those methods to access class variables and data
#              - For a class method, the class (cls) is the first argument instead of the instance (self)

class Employee:

    count = 0

    def __init__(self, name, position="Intern") -> None:
        self.name = name
        self.position = position
        Employee.count += 1

    @classmethod
    def get_employee_number(cls):
        return cls.count

employee1 = Employee("Jason", "Manager")
employee2 = Employee("Blake", "Janitor")

print(f"Number of employees: {Employee.get_employee_number()}")