'''
Imagine a stack of plates. If the stack gets too hight, it might topple.
Thus, we'd start a new stack when the previous stack exceeds a limit.
Implement a data structure SetOfStacks that mimics this. SetOfStacks 
should be composed of several stacks and shold create a new stack once
the previous one exceeds capacity. SetOfStacks.push and SetOfStacks.pop should
behave identically to single stack
'''

class StackInfo:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.stack = [-1 for i in range(capacity)]
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def push(self, value):
        self.stack.append(value)
        self.size += 1
    
    def pop(self):
        self.size -= 1
        return self.stack.pop()
    
    def peek(self):
        return self.stack[self.size - 1]

class SetOfStacks:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.current_stack = -1
        self.stacks = []
    
    def push(self, value):
        if len(self.stacks) == 0 or self.stacks[self.current_stack].is_full():
            self.create_new_stack()
        
        self.stacks[self.current_stack].push(value)

    def pop(self):
        if self.current_stack == -1:
            raise Exception("Stack is empty")
        value = self.stacks[self.current_stack].pop()
        if self.stacks[self.current_stack].is_empty():
            self.remove_stack_at()
        
        return value
    
    def peek(self):
        if self.current_stack == -1:
            raise Exception("Stack is empty")
        return self.stacks[self.current_stack].peek()
    
    def popAt(self, idx):
        if self.current_stack < idx:
            raise Exception("Stack does not exist")
        value = self.stacks[self.idx].pop()
        if self.stacks[self.idx].is_empty():
            self.remove_stack_at(idx)
        
        return value

    def create_new_stack(self):
        self.stacks.append([StackInfo(self.capacity) for i in range(self.limit)])
        self.current_stack += 1
    
    def remove_stack_at(self, idx = -1):
        self.stacks.pop(idx)
        self.current_stack -= 1
        
        

def solution(n):
    return False

def main():
    for test_case in []:
        print(solution(test_case))

if __name__ == "__main__":
    main()