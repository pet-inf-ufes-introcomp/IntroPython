#Questão 4

def is_palindrome(string1):
    l = int(len(string1)/2)
    
    for i in range(0, l):
        if string1[i] != string1[len(string1) - i - 1]:
            return False
    
    return True

def format_string(string1):
    string1 = string1.replace(" ", "")
    string1 = string1.lower()
    return string1

string1 = str(input())
string1 = format_string(string1)

print(is_palindrome(string1))
