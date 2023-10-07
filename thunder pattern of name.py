"""str=input()
length=len(str)
namePointer=0
for i in range(length-1,-1,-1):
    for j in range(i+1):
        if i==j:
            print(str[namePointer],end='')
            break
        else:
            print('',end=" ")
    namePointer+=1
    if i==0:
        print(str[-2:-length-1:-1])
        break
    print()
namePointer=1
for i in range(length-2,-1,-1):
    for j in range(i+1):
        if i==j:
            print(str[namePointer],end='')
            break
        else:
            print('',end=" ")
    namePointer+=1
    print()
"""
"""def pattern(str):
    for i in range(0,13):
        for j in range(0,7):
            if(((i==6) or i+j==6) or i+j==12):
                print(str[i],end=" ")
            else:
                print(" ",end=" ")
        print()
str=input()
len=len(str)
pattern(str)
"""
result_str=""
for row in range(0,13):    
    for column in range(0,7):     
        if (((row==6)  or row+column==6) or row+column==12):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)

