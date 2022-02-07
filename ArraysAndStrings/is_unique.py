def solution(s):
    # with data structures allowed, use hash map

    # python can't mutate strings in place. if it were a char array, could do quicksort
    s = sorted(s)
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            return False
    
    return True

def main():
    for test_case in ["abc", "aa", "aaa"]:
        print(solution(test_case))
    
if __name__ == "__main__":
    main()