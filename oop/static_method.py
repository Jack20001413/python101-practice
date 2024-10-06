class Employee:

    COEFFICIENTS_SALARY = 1.35

    def __init__(self, name, position, base_salary) -> None:
        self.name = name
        self.position = position
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary * Employee.COEFFICIENTS_SALARY
    
class SalaryConverter:

    @staticmethod
    def convert_to_usd(salary):
        return salary / 24609.99

employee = Employee("Jannie", "Manager", 20000000)    

print(SalaryConverter.convert_to_usd(employee.calculate_salary()))