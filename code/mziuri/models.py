class Member:
    def __init__(self, name, age, status, subject) -> None:
        self.name = name
        self.age = age  
        self.status = status
        self.subject = subject


class Teacher(Member):
    def __init__(self, name, age, status, salary):
        super().__init__(name, age, status, subject)
        self.__salary = salary



    def calculate_yearly_salary(self):
        return self.salary * 12 


class Student:
    def __init__(self, name, age,status, grade):
        super().__init__(self, name, age, status)
        self.grade = grade


    def __str__(self):
        return f"name: {self.name}"
    

shotiko = Teacher(
    "shotiko"
    21
    "Teacher"
    "Python"
    1000000
)

        