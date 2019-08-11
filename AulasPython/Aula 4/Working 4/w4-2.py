def par_ou_impar(n):
    if n%2 == 0:
        print('O numero e par')
    else:
        print('O numero e impar')

n = int(input())
while n != -1:
    par_ou_impar(n)
    n = int(input())
