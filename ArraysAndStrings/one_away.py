def solution(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    
    char_map = {}
    for i in a:
        if i not in char_map:
            char_map[i] = 0
        char_map[i] += 1
    
    num_differences = 0
    for i in b:
        if i not in char_map:
            char_map[i] = 0
            num_differences += 1
        if num_differences > 1:
            return False
        char_map[i] -= 1

    for i in char_map:
        if char_map[i] > 1 or char_map[i] < -1:
            return False

    return True

def main():
    for test_case in [("pale", "ple"), ("pales", "pale"), ("pale", "bale"), ("pale", "bake"), ("poke", "sake"), ("poke", "soke"), ("a", "b")]:
        print(solution(test_case[0], test_case[1]))

if __name__ == "__main__":
    main()