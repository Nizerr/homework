def init_(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

def greet(self):
    print("Hi, my name is", self.name)

def description(self):
    print(f"Person<{self.name}, {self.age}, {self.gender}>")

Student = type('Student', (object,), {
    'team': 'Python31',
    '__slots__': ['name', 'age', 'gender'],
    '__init__': init_,
    'greet': greet,
    'description': description
})

# Тестування класу Student
student = Student('Alice', 25, 'Female')
print(student.team)
student.greet()
student.description()