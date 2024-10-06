class Employee:

    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position

class Company:

    def __init__(self, name) -> None:
        self.name = name
        self.employees = []

    def add_employee(self, employee) -> None:
        self.employees.append(employee)

    def list_employees(self) -> Employee:
        return self.employees
    
    def count_employee(self) -> int:
        return self.employees.__len__()
    
company = Company("Irax")

employee1 = Employee("Janus", "IT Engineer")
employee2 = Employee("May", "Business Analyst")

company.add_employee(employee1)
company.add_employee(employee2)
print(f"Numbers of employees: {company.count_employee()}")

for employee in company.list_employees():
    print(f"{employee.name} - {employee.position}")