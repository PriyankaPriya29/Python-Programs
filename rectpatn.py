def pattern1(n=int(input('Enter a value:-'))): 
    for i in range(1,n+1): 
        for j in range(1,n+1): 
            if i==1 or i==n or j==1 or j==n :
                print('*',end="")
            else : 
                print('',end=" ")             
        print()
pattern1()
#output be lyk
#*****
#*   *
#*   *
#*   *
#*****
