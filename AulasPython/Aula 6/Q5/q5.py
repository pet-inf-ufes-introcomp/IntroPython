#Desafio 1

def format_string(string1):
    string1 = string1.replace(" ", "")
    string1 = string1.lower()
    return string1

def eh_subsequencia(string1,string2):
    string_test1 = format_string(string1)
    string_test2 = format_string(string2)
    list1        = list(string_test1)
    list2        = list(string_test2)
    
    dict1 = dict()
    dict2 = dict()
    
    for i in range(0, len(list1)):
        dict1[list1[i]] = 0
        
    for i in range(0, len(list2)):
        dict2[list2[i]] = 0
        
    for i in range(0, len(list1)):
        dict1[list1[i]] += 1
        
    for i in range(0, len(list2)):
        dict2[list2[i]] += 1
        
    if(dict1 == dict2):
        return True
        
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    
    if(set(keys1) < set(keys2) or len(keys2) > len(keys1)):
        return False
    
    for i in range(0, len(keys2)):
        j = keys2[i]
        if dict2[j] > dict1[j]:
            return False
        
    return True
    
string1 = str(input())
string2 = str(input())

print(eh_subsequencia(string1,string2))
