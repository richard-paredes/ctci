def solution(s):
    char_map = {}
    for char in s:
        if char not in char_map:
            char_map[char] = 0
        char_map[char] += 1
    
    string_builder = []
    for char in char_map:
        string_builder.append(char+str(char_map[char]))
    
    answer = "".join(string_builder)

    return answer if len(answer) < len(s) else s
    
    
# questions to ask
# is the string assumed to be sorted?
# does the order of the compression matter?
def main():
    for test_case in ["aaaabccccc"]:
        print(solution(test_case))

if __name__ == "__main__":
    main()