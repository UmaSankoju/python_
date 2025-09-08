
##operator overloading##
class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __add__(self, other):
        
        return FullName(self.first,other.last)

    def __str__(self):
        return f"{self.first} {self.last}"


name1 = FullName("Uma", "Sankoju")
name2 = FullName("Python", "Developer")

new_name = name1 + name2
print("Combined Name:", new_name)

##method Overloading##

class Factorial:
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

Fact = Factorial()
print(Fact.multiply(2, 3))          
print(Fact.multiply(2, 3, 4))       
print(Fact.multiply(1, 2, 3, 4, 5)) 

##method overriding##

class Employee:
    def work(self):
        print("Employee is working for Salary")

class Manager(Employee):
    def work(self):
        print("Manager is Working For Company")

class Developer(Employee):
    def work(self):
        print("Developer is Working For Creating APIs")


emp = Employee()
man = Manager()
dev = Developer()

emp.work()  
man.work()  
dev.work()  
