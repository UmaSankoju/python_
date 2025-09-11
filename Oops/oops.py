from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def get_role(self):
        pass
   
class Student(Person):
    def __init__(self, student_id,name,age):
        super().__init__(name,age)
        self.student_id=student_id
        self.enrolled_cources=[]
        
    def get_role(self):
        return Student
    def get_enrolled_cources(self):
        print(self.enrolled_cources)
        
    def add_a_course(self,course_name):
        if course_name not in self.enrolled_cources:
          self.enrolled_cources.append(course_name)
        else:
            pass
        
        
s1=Student("S001","XX",15)
s1.get_enrolled_cources()
s1.add_a_course("PYTHON")
s1.add_a_course("JAVA")
s1.add_a_course("DBMS")
s1.add_a_course("SQL")
s1.add_a_course("DJANGO")
s1.get_enrolled_cources()

class Teacher(Person):
    def __init__(self,teacher_id):
        self.teacher_id=teacher_id
        self.assaigned_cources=[]
        
    def get_role(self):
        return Teacher
    def get_assaigned_cources(self):
        print(self.assaigned_cources)
        
    def add_a_course(self,course_name):
        if course_name not in self.assaigned_cources:
          self.assaigned_cources.append(course_name)
        else:
            pass
t1=Teacher("T001")
t1.add_a_course("PYTHON")
t1.add_a_course("PYTHON")
t1.add_a_course("DJANGO")
t1.add_a_course(".NET")
t1.get_assaigned_cources()

class Course:
    def __init__(self,course_name,course_code):
        self.course_name=course_name
        self.course_code=course_code
        self.enrolled_students=[]
        self.teacher=None
    def set_techer(self,teacher_name):
        self.teacher=teacher_name
        
    def add_student(self,student_name):
        self.enrolled_students.append(student_name)
    def get_students(self):
        print(self.enrolled_students)
        
    def show_details(self):
        print("course details:\n","course name:",self.course_name,"\ncourse code:",self.course_code)
    
c1=Course("python","c001")
c1.add_student("Jane")
c1.add_student("John")
c1.add_student("Doe")
c1.add_student("Manu")
c1.add_student("Ramu")
c1.show_details()
c1.get_students()
    
class Department:
    def __init__(self):
        
        self.dept_list=[]
        self.teachers=[]
        self.students=[]
        
    def add_dept(self,dept_name):
        self.dept_list.append(dept_name)
    def get_dept_list(self):
        print(self.dept_list)
        
    def add_teachers(self,teacher_name):
        self.teachers.append(teacher_name)
    def get_teachers(self):
        print(self.teachers)
        
    def add_students(self,student_name):
        self.students.append(student_name)
    def get_students(self):
        print(self.students)
        
    def show_details(self):
        print("depatment details:")
d1=Department()
d1.add_dept("Block-1")
d1.add_students("john")
d1.add_teachers("jake")
d1.show_details()
d1.get_teachers()
d1.get_students()
d1.get_dept_list()
d1.show_details()
class Administration:
    def __init__(self):
        self.dept_list=[]
        
    def add_dept(self,dept_name):
        self.dept_list.append(dept_name)
    def get_dept_list(self):
        
       print(self.dept_list)
        
    def show_details(self):
        print("list of the deparments in administration:",self.dept_list)

a1=Administration()
a1.add_dept("Block-A")
a1.get_dept_list()
a1.show_details()