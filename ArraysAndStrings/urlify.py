def solution(s, l):
    num_spaces = 0
    for i in range(l):
        if s[i].isspace():
            num_spaces += 1
    
    idx = l + num_spaces * 2
    string_builder = [c for c in s]
    for i in range(l - 1, -1, -1):
        if string_builder[i].isspace():
            string_builder[idx - 1] = '0'
            string_builder[idx - 2] = '2'
            string_builder[idx - 3] = '%'
            idx -= 3
        else:
            string_builder[idx - 1] = string_builder[i]
            idx -= 1
    
    return "".join(string_builder)

def solution_alt(s, l):
    return "%20".join(s.split())

def main():
    for test_case in [("Mr John Smith    ", 13)]:
        print(solution(test_case[0], test_case[1]))

if __name__ == "__main__":
    main()