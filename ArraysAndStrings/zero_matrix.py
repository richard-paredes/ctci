def solution(m):
    num_rows = len(m)
    num_cols = len(m[0])
    rows_to_change = set()
    columns_to_change = set()

    '''
    optimization:
    Instead of using two arrays to track rows & cols
    we could use the first row and the first column of
    the matrix.
    If and only if the row has a zero, we will just put a zero
    in that first row
    Likewise, the same for the columns
    It doesn't matter if we overwrite the data because 
    it's going to be zeroed out. We don't overwrite it
    if it does not have a zero!!
    '''

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                rows_to_change.add(i)
                columns_to_change.add(j)
    
    for row in rows_to_change:
        for col in range(num_cols):
            m[row][col] = 0
    
    for col in columns_to_change:
        for row in range(num_rows):
            m[row][col] = 0
        
    return m


def main():
    for test_case in [
        [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [9, 10, 11]
        ],
        [
            [1, 2, 3, 1],
            [4, 0, 5, 1],
            [6, 7, 8, 1]
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ]:
        for i in solution(test_case):
            print(i)
        print()

if __name__ == "__main__":
    main()