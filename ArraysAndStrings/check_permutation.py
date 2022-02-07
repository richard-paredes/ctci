def solution(a, b):
    if len(a) != len(b): 
        return False
    char_map = {}
    for char in a:
        if char not in char_map:
            char_map[char] = 0
        char_map[char] += 1
    
    for char in b:
        if char not in char_map:
            return False
        char_map[char] -= 1
        if char_map[char] < 0: 
            return False
        
    return True


def main():
    for test_case in [("abc", "bca"), ("asd", "aaa")]:
        print(solution(test_case[0], test_case[1]))

if __name__ == "__main__":
    main()