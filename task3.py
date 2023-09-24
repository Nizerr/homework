class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        if self.capacity + v <= self.capacity:
            return True
        return False

    def add(self, v):
        if self.can_add(v):
            self.count += v
        else:
            print(f"Не можна добавити {v} монет")



box = MoneyBox(10)
box.add(6)