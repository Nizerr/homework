class Student:

    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def __repr__(self):
        return f"Repr: {self.name} - {self.scores}"

    def __getitem__(self, index):
        return self.scores[index]

    # Заміна оцінки
    def __setitem__(self, index, value):
        self.scores[index] = value

    def __delitem__(self, index):
        print(f"del index {index}")
        del self.scores[index]

    def __getattr__(self, item):
        print("get attribute")

    def __getattribute__(self, item):
        print("Get attribute")

A = Student("Alice", [5, 6, 8, 12])
print(A.age)
# print(A.scores[0])
# print(A[0])
# print(*A)
# A[0] = 12