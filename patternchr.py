n=int(input('Enter a number:-'))
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=" ")
        else:
            print(' ',end=" ")
        print()
#chr(97)
#ord('a')
#round(357.90,3)
n=int(input('Enter a number:-'))
for i in range(1,n+1):
    for k in range(n-i,0,-1):
        print(' ',end="")
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end="")
        else:
            print(' ',end="")
    print()
