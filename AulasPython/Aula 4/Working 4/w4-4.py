caminho = 'char.txt'
M = 0
m = 0
with open(caminho, "r") as f:
    c = f.read(1)
    while c:
        if c != ';':
            if c.isupper():
                M += 1
            elif c.islower():
                m += 1
        c= f.read(1)
print("{} {}".format(M,m))
