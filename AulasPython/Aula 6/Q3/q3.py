#Questão 3
def is_palindrome(string1):
    l = int(len(string1)/2)
    
    for i in range(0, l):
        if string1[i] != string1[len(string1) - i - 1]:
            return False
    
    return True

string1 = str(input())
print(is_palindrome(string1))
