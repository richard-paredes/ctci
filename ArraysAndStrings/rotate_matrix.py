def solution(m):
    for layer in range(len(m) // 2):
        first = layer
        last = len(m) - 1 - layer

        for i in range(first, last):
            offset = i - first

            top = m[first][i]

            # left -> top
            m[first][i] = m[last - offset][first]

            #bottom -> left
            m[last - offset][first] = m[last][last - offset]

            # right -> bottom
            m[last][last - offset] = m[i][last]

            # top -> right
            m[i][last] = top
    
    return m


def main():
    for test_case in [
        [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
    ]:
        for i in test_case:
            print(i)
        print()
        for i in solution(test_case):
            print(i)
        print()

if __name__ == "__main__":
    main()
    
