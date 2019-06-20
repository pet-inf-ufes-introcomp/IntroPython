import sys


def print_matrix(matrix):
    write = sys.stdout.write

    w = len(matrix[0])
    h = len(matrix)

    for i in range(0, h):
        for j in range(0, w):
            write(str(matrix[i][j]) + " ")
        write("\n")


def main():
    x, y = input().split( )
    x = int(x)
    y = int(y)

    if x <= 0 or y <= 0:
        return

    matrix = [[0 for i in range(x)] for j in range(y)]

    print_matrix(matrix)


if __name__ == '__main__':
    main()
