
f = open('notas.txt', 'r')
maior = -1
menor = 11
soma = 0
N = int(f.readline())
for i in range(N):
    nota = float(f.readline())
    if nota > maior: maior = nota
    if nota < menor: menor = nota
    soma += nota

f.close()
print('{:.2f} {:.2f} {:.2f}'.format(maior, menor, soma/N))
