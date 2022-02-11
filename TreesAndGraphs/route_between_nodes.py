'''
Given a directed graph, design an algorithm to find out whether there is
a route between two nodes
'''

def depth_first_search(graph, visited, node, end):
    if node == end:
        return True
    
    for neighbor in graph[node]:
        if neighbor in visited:
            continue
        visited.add(neighbor)
        if depth_first_search(graph, visited, neighbor, end):
            return True
    
    return False

def breadth_first_search(graph, start, end):
    queue = [start]
    visited = set()

    while len(queue) > 0:
        node = queue.pop(0)
        if node == end:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            queue.append(neighbor)
    
    return False

def solution(graph, start, end):
    return breadth_first_search(graph, start, end) and depth_first_search(graph, set(), start, end)

def main():
    for test_case in [
        ({
            0: [1],
            1: [2],
            2: [3],
            3: []
        }, 0, 3),
        ({
            0: [1],
            1: [2],
            2: [3],
            3: []
        }, 2, 0)
    ]:
        print(solution(test_case[0], test_case[1], test_case[2]))

if __name__ == "__main__":
    main()