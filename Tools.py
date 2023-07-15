# Todo: merge this content somewhere else

def matrixOfFalse():
    # create matrix of 3x3 (with 3 char string)
    row = [False for x in 'abc']
    matrix = [row.copy() for x in 'abc'] # deep copy is needed
    assert matrix == [ [False, False, False], [False, False, False], [False, False, False] ]

    # Change 1st row, 2nd column
    matrix[1][2] = True
    assert matrix == [ [False, False, False], [False, False, True], [False, False, False] ]

def main():
    matrixOfFalse()

if __name__ == '__main__':
    main()
    print('Tests passed!')
