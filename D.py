
class TextFileOperations:
    def __init__(self,path):
        self.path = path

    def read_text_data(self):
        with open(self.path, 'r') as file:
            data = file.read()
        return data

    def write_text_data(self, data):
        with open(self.path,'w') as file:
            file.write(data)

class TextOperations:
    def __init__(self, text_source):
        self.text_source = text_source
        self.data = self.text_source.read_text_data()

    def search_for_word(self, word):
        return word in self.data

    def count_occurences(self, word):
        return self.data.count(word)

file = TextFileOperations("data.txt")

obj = TextOperations(file)
print(f"{obj.search_for_word('more')}")
print(f"{obj.count_occurences('y')}")