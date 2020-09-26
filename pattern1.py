n=int(input('Enter a number:-'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=" ")
    print()
n=int(input('Enter a number:-'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()
n=int(input('Enter a number:-'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#1st output be lyk
    #* * * * *
    #* * * * * 
    #* * * * *
#2nd output be lyk
    #* 
    #* * 
    #* * * 
    #* * * * 
    #* * * * *  
#3rd output be lyk
    #1 
    #1 2 
    #1 2 3 
    #1 2 3 4 
    #1 2 3 4 5
