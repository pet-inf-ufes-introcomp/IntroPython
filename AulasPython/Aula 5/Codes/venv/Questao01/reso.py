import sys

def printMatrix(matrix):
    write = sys.stdout.write
    for i in range(0, 3):
        for j in range(0, 3):
            write(str(matrix[i][j]) + " ")
        write("\n")

def main():
    a, b, c, d, e, f, g, h, i = input().split( )

    matrix = [[a, b, c], [d, e, f], [g, h, i]]

    printMatrix(matrix)


if __name__ == '__main__':
    main()
