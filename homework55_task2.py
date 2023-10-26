from homework55_task1 import Stack

def check_brackets(input_string):
    stack = Stack()

    for char in input_string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False  # Закриваюча дужка без відповідної відкриваючої
            stack.pop()

    return stack.is_empty()


print(check_brackets("((()))"))
print(check_brackets("(()()())"))
print(check_brackets("((())"))
print(check_brackets("())("))