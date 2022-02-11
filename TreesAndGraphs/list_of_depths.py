'''
Given a binary tree, design an algorithm which creates a linked list
of all the nodes at each depth (e.g. if you have a tree with depth D,
you'll have D linked lists)
'''
class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left = left_child
        self.right = right_child

class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def traverse_dfs(node, depth_map={}, height=0):
    if node is None:
        return
    
    if height not in depth_map:
        depth_map[height] = []
    
    depth_map[height].append(node)
    traverse_dfs(node.left, depth_map, height + 1)
    traverse_dfs(node.right, depth_map, height + 1)

def traverse_bfs(node, depth_map={}, height=0):
    queue = [(node, height)]

    while len(queue) > 0:
        (current, height) = queue.pop()
        
        if height not in depth_map:
            depth_map[height] = []
        depth_map[height].append(current)

        queue.append((current.left, height + 1))
        queue.append((current.right, height + 1))

def create_linked_lists(depth_map):
    linked_lists = []
    for height in depth_map:
        start = LinkedListNode(depth_map[height].pop())
        current = start
        while len(depth_map[height]) > 0:
            current.next = LinkedListNode(depth_map[height].pop())
            current = current.next
        linked_lists.append(start)
    
    return linked_lists


def solution(root):
    depth_map = {}
    # traverse_dfs(root, depth_map)
    traverse_bfs(root, depth_map)
    return create_linked_lists(depth_map)

def main():
    for test_case in []:
        print(solution(test_case))

if __name__ == "__main__":
    main()