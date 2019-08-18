#Questão 2
def is_in_interval(num1, num2, num):
    if(num1 <= num and num2 >= num):
        return True
    else:
        return False
    
num1 = int(input())
num2 = int(input())
num  = int(input())

print(is_in_interval(num1, num2, num)
