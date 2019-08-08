def main():

    n = int(input())

    lista = []

    for i in range(n):
        name, age, crn = input().split()
        age = int(float(age))
        crn = float(crn)
        tupla = (name, age, crn)
        lista.append(tupla)

    for i in range(n):
        print(lista[i][1], lista[i][0], lista[i][2])


if __name__ == '__main__':
    main()
