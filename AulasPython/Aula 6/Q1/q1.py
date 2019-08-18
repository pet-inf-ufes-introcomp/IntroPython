#Questão 1
def string_inverter(string1):
    string2 = ''
    for i in range(1, len(string1) + 1):
        string2 += string1[len(string1) - i]
    return string2

string1 = str(input())
print(string_inverter(string1))
