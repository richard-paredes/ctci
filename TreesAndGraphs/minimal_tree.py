'''
Given a sorted (asc) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height
'''
class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left = left_child
        self.right = right_child
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __inorder(self, node=None):
        if node is None:
            return
        self.inorder(node.left_child)
        print(node.value)
        self.inorder(node.right_child)
    
    def inorder(self):
        self.__inorder(self.root)
    
    def __min_value(self, node=None):
        while node.left is not None:
            node = node.left
        return node
    
    def __add(self, value, node=None):
        if node is None: 
            return TreeNode(value)
        if value < node.value: 
            node.left_child = self.__add(node.left_child, value)
        elif value > node.value: 
            node.right_child = self.__add(node.right_child, value)
        return node
    
    def add(self, value):
        if self.root is None: 
            self.root = TreeNode(value)
        else:
            self.root = self.__add(value, self.root)
    
    def __remove(self, value, node=None):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self.__remove(value, node.left)
        elif value > node.value:
            node.right = self.__remove(value, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            if node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.__min_value(node.right)
            node.value = temp.value
            node.right = self.__remove(value, node.right)
        
        return node
    
    def remove(self, value):
        return self.__remove(value, self.root)

    def __search(self, value, node=None):
        if node is None:
            return None
        if value == node.value:
            return node
        if value < node.value:
            return self.__search(value, node.left)
        if value > node.value:
            return self.__search(value, node.right)

    def search(self, value):
        return self.search(self, value, self.root)

def createMinimalTree(array, start, end):
    if start > end:
        return None
    
    midpoint = len(end - start) // 2
    node = TreeNode(array[midpoint])
    node.left = createMinimalTree(array, start, midpoint - 1)
    node.right = createMinimalTree(array, midpoint + 1, end)
    
    return node

def solution(array):
    return createMinimalTree(array, 0, len(array))

def main():
    for test_case in []:
        print(solution(test_case))

if __name__ == "__main__":
    main()