from functools import reduce
from math import factorial
'''
A binary search tree was created by traversing through an array
from left to right and inserted each element. Given a binary search tree
with distinct elements, print all possible arrays that could have
led to this tree
'''

'''
So imagine we have a tree like this:

    A
That means the array was created by [A]

Now imagine we have a tree like this:

    B
A
That means the array was created by: [B, A]. There's no way it was [A, B]!

Now imagine we have a tree like this:
    C
B       A
That means the array was created by: [C, B, A] OR [C, A, B].

Now imagine we have a tree like this:
        D
    C
B       A
That means it could have been created by:
    [D, C, B, A] OR [D, C, A, B]

Now imagine we have a tree like this:
        D
    C       B
A
That means it could have been created by:
    [D, C, B, A] OR [D, B, C, A] OR [D, C, A, B]


Now imagine we have a tree like this:
                A
        B               C
    D       E

[A, B, D, E, C]
[A, B, E, D, C]
[A, B, C, D, E]
[A, B, C, E, D]


Now imagine we have a tree like this:
                A
        B               C
    D       E       F

A
BC, CB
DEF, DFE, EFD, EDF, FED, FDE

[A, B, C, D, E, F]
[A, B, C, D, F, E]
[A, B, C, E, F, D]
[A, B, C, E, D, F]
[A, B, C, F, E, D]
[A, B, C, F, D, E]
[A, C, B, D, E, F]
[A, C, B, D, F, E]
[A, C, B, E, F, D]
[A, C, B, E, D, F]
[A, C, B, F, E, D]
[A, C, B, F, D, E]
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_array(builder, depth_map, current_height, solutions):
    options = [] if current_height not in depth_map else depth_map[current_height]
    if (len(options) == 0):
        solutions.append(builder)
        return
    for i in range(len(options)):
        create_array(builder + options[i], depth_map, current_height + 1, solutions)

def addperm(x,l):
    return [ l[0:i] + [x] + l[i:]  for i in range(len(l)+1) ]

def permute(l):
    if len(l) == 0:
        return [[]]
    return [x for y in permute(l[1:]) for x in addperm(l[0],y) ]

def build_depth_map(node, height = 0, depth_map = {}):
    if node is None:
        return
    if height not in depth_map:
        depth_map[height] = []
    depth_map[height].append(node.value)
    build_depth_map(node.left, height + 1, depth_map)
    build_depth_map(node.right, height + 1, depth_map)

def solution(root):
    depth_map = {}
    build_depth_map(root,0, depth_map)
    x = reduce(lambda product, current: factorial(len(depth_map[current]))*product, depth_map, 1)
    for i in depth_map:
        depth_map[i] = permute(depth_map[i])
    solutions = []
    create_array([], depth_map, 0, solutions)
    print(solutions)
    return False

def main():
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.left = Node('F')
    for test_case in [root]:
        print(solution(test_case))

if __name__ == "__main__":
    main()
