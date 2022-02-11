def is_substring(a, b):
    return b in a

def contains_same_chars(a, b):
    char_map = a
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
        
    for char in char_map:
        if char_map[char] > 0:
            return False
            
    return True

def solution(a, b):
    if len(a) != len(b) or len(a) <= 0:
        return False
    
    return is_substring(a+a, b)

def main():
    for test_case in [
        ("waterbottle", "erbottlewat"), 
        ("waterbottle", "bottlewater"), 
        ("water", "terwa")]:
        print(solution(test_case[0], test_case[1]))
    
if __name__ == "__main__":
    main()