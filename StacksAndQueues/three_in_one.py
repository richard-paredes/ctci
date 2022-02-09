'''
Describe how you could use a single array to implement three stacks

Option 1: 
Have the single array be partitioned equally. Each partition represents a stack
'''
class StackInfo:

    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
    
    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0

class O1_MultiStack:
        
    def __init__(self, capacity, num_stacks = 3):
        self.num_stacks = num_stacks
        self.stack_infos = [StackInfo(i, capacity) for i in range(num_stacks)]
        self.array = [-1 for i in range(capacity * num_stacks)]

    def get_stack_position(self, stack_num, idx):
        return  stack_num * self.stack_infos[stack_num].capacity + idx

    def push(self, stack_num, value):
        if self.stack_infos[stack_num].is_full():
            raise Exception("Stack is full")
        
        idx = self.get_stack_position(stack_num, self.stack_infos[stack_num].size)
        self.array[idx] = value
        self.stack_infos[stack_num].size += 1
    
    def pop(self, stack_num):
        if self.stack_infos[stack_num].is_empty():
            raise Exception("Stack is empty")
        
        idx = self.get_stack_position(stack_num, self.stack_infos[stack_num].size - 1)
        value = self.array[idx]
        self.array[idx] = -1
        self.stack_infos[stack_num].size -= 1
        return value
    
    def peek(self, stack_num):
        if self.stack_infos[stack_num].is_empty():
            raise Exception("Stack is empty")
        
        idx = self.get_stack_position(stack_num, self.stack_infos[stack_num].size - 1)
        return self.array[idx]

def solution(n):
    return False

def main():
    for test_case in []:
        print(solution(test_case))

if __name__ == "__main__":
    main()