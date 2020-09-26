def pattern(n):
    for i in range(0,n):
        for j in range(n-1,i,-1):
            print('*',end=" ")
        for k in range(0,n):
            print(' ',end="")
        print()
n=int(input('Enter a value:-'))
pattern(n)
#output be lyk
#* * * *      
#* * *      
#* *      
#*      
  







#ABCDE
#ABCDE
#ABCDE
#FOR I IN RANGE(5):
    #PRINT('ABCDE')
 

