# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
str1 = input()#Taking first input
str2 = input()#Taking second input

print("\n")

str1 = str1.replace(" ","")#Making it into one string
str2 = str2.replace(" ","")#Making it into one string

MAX_CHAR = 256

str = str1 + str2

n_count = len(str)

distinct_char = []

def distinctChar(str):
    count = [0] * MAX_CHAR
    
    for i in range(len(str)):
        if(str[i] != ' '):
            count[ord(str[i])] += 1
    n = i
    
    for i in range(n):
        if(count[ord(str[i])] == 1):
            print(str[i], end = "")
            distinct_char.append(str[i])

distinctChar(str)
distinct_count = len(distinct_char)

flames = "flames"  # initializing string of flames

total_flame_count = len(flames)

def cancel_letter(n_count,total_flame_count): # recursive function to find the exact index number in string "flames" in one time
    if(n_count <= total_flame_count):
        return n_count
    n_count = n_count - total_flame_count
    if(n_count >= 1 and n_count <= total_flame_count):
        return n_count
    else:
        return cancel_letter(n_count,total_flame_count)


for i in range(0,5): # loop of 5 times because in string "flames" maximum number of times we have to loop is 5 ie we have to cut element maximum for 5 times
    #print("total flame count --> "+str(total_flame_count))
    #print("i--> "+str(i))
    index_number = cancel_letter(distinct_count,total_flame_count)
    index_number = index_number-1
    #print("index_number --> "+str(index_number))
    flames = flames.replace(flames[index_number], "")
    #print(flames)
    total_flame_count = total_flame_count - 1
    #print("\n")
    
# NOTE : - whene ever you want to check flow of the program just remove comment of print statements.
    

if(flames=="f"):
    print("\n")
    print("FRIEND")
elif(flames=="l"):
    print("\n")
    print("LOVE")
elif(flames=="a"):
    print("\n")
    print("AFFAIR")
elif(flames=="m"):
    print("\n")
    print("MARRIAGE")
elif("e"):
    print("\n")
    print("ENEMY")
elif("s"):
    print("\n")
    print("SEX")
