def main():

    alunos = {" ": 0}
    maior_aluno = " "

    while True:
        entrada = input()
        if entrada == "oooo":
            break

        key, value = entrada.split( )

        key = str(key)
        value = float(value)

        alunos[key] = value
        if value > alunos[maior_aluno]:
            maior_aluno = key

    print(maior_aluno)


if __name__ == '__main__':
    main()
