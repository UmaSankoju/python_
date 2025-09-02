class Employee:
    # Class variable (shared among all employees)
    company_name = "TechCorp Pvt Ltd"
    employee_count = 0

    # Constructor
    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    # Instance method
    def show_details(self):
        print(f"Employee: {self.name}\nSalary: ₹{self.salary}")

    # Class method
    @classmethod
    def show_company_info(cls):
        print(f"Company: {cls.company_name}\nTotal Employees: {cls.employee_count}")

    # Static method
    @staticmethod
    def is_high_salary(salary):
        return salary > 50000


# Creating objects (constructor runs automatically)
e1 = Employee("Ankit", 45000)
e2 = Employee("jay", 65000)
e3 = Employee("Ava", 55000)
e4 = Employee("Rishi", 60000)
e5 = Employee("harsha", 65000)

# Instance method calls
e1.show_details()
e2.show_details()
e3.show_details()
e4.show_details()
e5.show_details()


# Class method call
Employee.show_company_info()

# Static method call
print("Does Ankit have a high salary? \n", Employee.is_high_salary(e1.salary))
print("Does Neha have a high salary? \n", Employee.is_high_salary(e2.salary))
print("Does Neha have a high salary? \n", Employee.is_high_salary(e3.salary))
print("Does Neha have a high salary? \n", Employee.is_high_salary(e4.salary))
print("Does Neha have a high salary? \n", Employee.is_high_salary(e5.salary))