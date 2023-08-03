# Python program to reverse a stack with O(1)
# space using recrusion in mem call

def insertAtBottom(stack, item):
	if stack.isEmpty():
		stack.push(item)
	else:
		temp = stack.pop()
		insertAtBottom(stack, item)
		stack.push(temp)

def reverse(stack):
	if not stack.isEmpty():
		temp = stack.pop()
		reverse(stack)
		insertAtBottom(stack, temp)

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow ")
            exit(1)
        return self.stack.pop()

    def prints(self):
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i], end=' ')
        print()


stack = Stack()
stack.push(str(4))
stack.push(str(3))
stack.push(str(2))
stack.push(str(1))
print("Original Stack ")
stack.prints()
reverse(stack)
print("Reversed Stack ")
stack.prints()

