'''
T1 and T2 are two very large binary trees, with T1 much bigger
than T2. Create an algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that
the subtree of n is identical to T2. That is, if you cut off the
tree at node n, the two trees would be identical
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def are_equal(main, sub):
    if main is None and sub is None:
        return True
    if main is None or sub is None:
        return False
    return main.value == sub.value and
        are_equal(main.left, sub.left) and
        are_equal(main.right, sub.right)

def is_subtree(main_root, subtree_root):
    if subtree_root is None:
        return True
    if main_root is None:
        return False

    if are_equal(main_root, subtree_root):
        return True

    return is_subtree(main_root.left, subtree_root) or
        is_subtree(main_root.right, subtree_root)

def solution(t, s):
    return is_subtree(t, s)

def main():
    for test_case in []:
        print(solution(test_case))

if __name__ == "__main__":
    main()
