def multiply_matrixes(a, b):

    c = [[1, 2, 3],
         [1, 2, 3],
         [1, 2, 3]]

    for i in range(3):
        for j in range(3):
            c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j] + a[i][2] * b[2][j]

    return c


def create_matrixes():
    a = input().split()
    b = input().split()

    ma = [[int(a[0]), int(a[1]), int(a[2])],
          [int(a[3]), int(a[4]), int(a[5])],
          [int(a[6]), int(a[7]), int(a[8])]]

    mb = [[int(b[0]), int(b[1]), int(b[2])],
          [int(b[3]), int(b[4]), int(b[5])],
          [int(b[6]), int(b[7]), int(b[8])]]

    return multiply_matrixes(ma, mb)

def main():
    print(create_matrixes())


if __name__ == '__main__':
    main()
