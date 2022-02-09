'''
How would you design a stack which, in addition to push and pop, has a function 
which returns the minimum element? Push, pop, and min should all operate in O(1)
time
'''

import sys


class MinStack:
    def __init__(self):
        self.mins = []
        self.stack = []

    def push(self, value):
        if value < self.min():
            self.mins.append(value)
        self.stack.append(value)
    
    def pop(self):
        value = self.stack.pop()
        if value <= self.min():
            self.mins.pop()
        return value
    
    def min(self):
        if len(self.mins) == 0:
            return sys.maxsize
        return self.mins[len(self.mins) - 1]


def solution(n):
    return False

def main():
    for test_case in []:
        print(solution(test_case))

if __name__ == "__main__":
    main()