def main():
    x, y = input().split( )
    x = int(x)
    y = int(y)

    if x <= 0 or y <= 0:
        return

    matrix = [[0 for i in range(x)] for j in range(y)]

    print(matrix)


if __name__ == '__main__':
    main()
