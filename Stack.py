'''A stack is a linear data structure that follows LIFO(Last in first out).
The element inserted last will removed first'''
#Stack imimplementation using clam
class Stack:
    def __init__(self, n):
        self.stack = []
        self.n = n  #n = maxium number of elements inserted in this stack

        
    def push(self, k):
        #k is the value to be pushed.
        if len(self.stack) < self.n:
            self.stack.append(k)
        else: 
            print('Stack is full')

    def pop(self):
        if len(self.stack) == 0:
            print('The stack is empty')
        else:
            self.stack.pop(-1)#This will delete the last element
        
        self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            print('Stack is empty')

        else:
            return self.stack[-1]#It will return the last element

    def size(self):
        return len(self.stack)
    
    def display(self):
        print(self.stack)#Shows stack content


s = Stack(3)#Stack capacity changed to 3
s.display()
print(f'\n Size of stack :{s.size()}')
s.push(5)
s.display()
print(f'\n Size of stack is: {s.size()}')

s.push(10)
s.display()
print(f'\n Size of stack is: {s.size()}')

s.push(15)
s.display()
print(f'\n Size of stack is: {s.size()}')

s.push(25)
s.display()
print(f'\n Size of stack is: {s.size()}')

#Remove top elements
s.pop()
s.display()
print(f'\n Size of stack is: {s.size()}')


print(s.top(),' \n-----------------------------\n')
