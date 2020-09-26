def pattern(n=int(input('Enter a value:-'))):
    for i in range(1,n+1):
        for j in range(n-1,0):
            if i==1 or i==n or j==1 or j==n:
                print('*',end=" ")
        print()
pattern()
