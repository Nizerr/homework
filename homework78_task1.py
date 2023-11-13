class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self  # Повертає самого себе як ітератор

    def __next__(self):
        if self.current <= self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

my_range = MyRange(1, 5)

for num in my_range:
    print(num)