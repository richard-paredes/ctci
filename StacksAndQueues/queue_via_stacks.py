'''
Implement a MyQueue class which implements a queue using two stacks
'''

class Stack:
    def __init__(self, capacity = 10):
        self.capacity = 10
        self.arr = []
    
    def is_full(self):
        return len(self.arr) == self.capacity
    
    def is_empty(self):
        return len(self.arr) == 0
    
    def push(self, value):
        if self.is_full():
            raise Exception("Stack is full")
        
        self.arr.append(value)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.arr.pop()
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.arr[-1]

class MyQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.oldest_elements = Stack(capacity)
        self.newest_elements = Stack(capacity)

    def queue(self, value):
        if self.is_full():
            raise Exception("Queue is full")
        
        self.newest_elements.push(value)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.shift()
        return self.oldest_elements.pop()
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.shift()
        return self.oldest_elements.peek()
        
    def shift(self):
        if len(self.oldest_elements) == 0:
            while len(self.newest_elements) > 0:
                self.oldest_elements.append(self.newest_elements.pop())
    
    def is_empty(self):
        return len(self.newest_elements) == 0 and len(self.oldest_elements) == 0
    
    def is_full(self):
        return len(self.newest_elements) == self.capacity or len(self.oldest_elements) == self.capacity

def solution(n):
    return False

def main():
    for test_case in []:
        print(solution(test_case))

if __name__ == "__main__":
    main()