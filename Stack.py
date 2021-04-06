class Stack:
    #Constructor 
    def __init__(self):
        self.elements = []
    #Returns the top of the stack
    def top (self):
        return self.elements[len(elements) - 1]
    #Removes the top of the stack and returns it
    def pop (self):
        return self.elements.pop()
    #Adds an elements into the stack
    def push(self, num):
        return self.elements.append(num)
    #Checks if the stack is empty
    def is_empty(self):
        return not self.elements
    #Return the stack as a string
    def __str__(self):
        if self.elements:
            hold = ' '
            for x in range(len(self.elements)):
                hold = hold + str(self.elements[x]) + ' '
            hold ='[' + hold + ']'
        else:
            hold = '[ ]'
        
        return hold
#Creating an object
stack = Stack()

#Test
print('is_empty():', stack.is_empty())
print('empty:', stack)
stack.push(1)
print('after push(1):', stack)
print('is_empty():', stack.is_empty())
stack.push(10)
print('after push(10):', stack)
print('pop():', stack.pop())
print('after pop():', stack)
stack.push(2)
print('after push(2):', stack)
stack.push(3)
print('after push(3):', stack)
stack.push(4)
print('after push(4):', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('is_empty():', stack.is_empty())