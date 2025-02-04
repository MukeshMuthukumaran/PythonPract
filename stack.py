class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(f"Pushed {value} onto the stack.")

    def pop(self):
        if not self.is_empty():
            popped_value = self.stack.pop()
            print(f"Popped {popped_value} from the stack.")
            return popped_value
        else:
            print("Stack is empty, cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty, cannot peek.")
            return None

    def is_empty(self):
        return len(self.stack) == 0


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(f"Top element is {stack.peek()}")
stack.pop()
print(f"Top element after pop is {stack.peek()}")
print(f"Is the stack empty? {stack.is_empty()}")
stack.pop()
stack.pop()
stack.pop()
