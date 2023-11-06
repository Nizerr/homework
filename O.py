import os
from abc import abstractmethod, ABC

class IOutput(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def display(self):
        pass

class ConsoleOutPut(IOutput):

    def display(self):
        print(f"{self.data}")

class FileOutput(IOutput):
    def display(self):
        with open('output332.txt', 'w') as f:
            # Write the data to the file.
            f.write(self.data)

obj = ConsoleOutPut("some string")
obj.display()

obj_to_file = FileOutput("some string to file")
obj_to_file.display()