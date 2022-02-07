def solution(s):
    char_map = {}
    length_without_whitespace = 0

    for i in s.lower():
        if i.isspace():
            continue
        if i not in char_map:
            char_map[i] = 0
        char_map[i] += 1
        length_without_whitespace += 1
    if length_without_whitespace % 2 == 0:
        # do something
        for i in char_map:
            if char_map[i] % 2 == 1:
                return False
    else:
        num_odd_chars = 0
        for i in char_map:
            if char_map[i] % 2 == 1:
                num_odd_chars += 1
            if num_odd_chars > 1:
                return False
    
    return True


def main():
    for test_case in ["Tact Coa", "bob", "boobb", "", "   "]:
        print(solution(test_case))

if __name__ == "__main__": 
    main()