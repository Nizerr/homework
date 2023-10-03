class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f" Мені {self.name}, {self.age} років"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_it = student_id

    def stydy(self, subject):
        return f"Студент {self.name}-{self.student_it} навчається {subject}"

    def introduce(self):
        return f"Студент {self.name}, {self.age} Років і вчитель"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self, student):
        if isinstance(student, Student):
            return f"Вчитель {self.name} викладає {self.subject} студует {self.name}"
        else:
            return f"{self.name} не може навчате {student.name}, тому що вони не студенти"

    def introduce(self):
        return f"Я {self.name} мені {self.age} і я вчитель"

class Employee(Person):
    def __init__(self, name, age, salary, specialty):
        super().__init__(name, age)
        self.salary = salary
        self.specialty = specialty

    def work(self):
        return f"{self.name} працює як {self.specialty} отримує зарплата {self.salary}"

    def introduce(self):
        return f"Мені {self.name}, {self.age} років і я працюю"


student = Student("Alice", 20, "12345")
teacher = Teacher("Mr. Smith", 35, "Mathematics")
employee = Employee("John", 30, 50000, "Software Developer")

print(student.introduce())
print(teacher.introduce())
print(teacher.teach(student))
print(employee.introduce())
print(employee.work())