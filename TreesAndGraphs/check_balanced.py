'''
Implement a function to check if a binary is balanced. For the purpose of this
question, a balanced tree is defined to be a tree such that the heights of the two
subtrees of any node never differ by more than one
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
'''
We need to check that the left child's height is 
no more than abs(1) different than the right
child's height

So, height(n.left) - height(n.right) <= abs(1)

We need to do this for each subtree...

Start at the leaf nodes and work up...

So height() is recursive. It checks.
if it's a leaf node, return 0
if it's not, get the height of subtree + 1
'''
def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


def is_balanced(node):
    if node is None:
        return True
    left_height = height(node.left)
    right_height = height(node.right)
    return abs(left_height - right_height) <= 1 and is_balanced(node.left) and is_balanced(node.right)

def solution(root):
    return is_balanced(root)

def main():
    for test_case in []:
        print(solution(test_case))

if __name__ == "__main__":
    main()
