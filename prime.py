a=int(input('Enter starting range:'))
b=int(input('Enter ending range:'))
for j in range(a,b+1):
    for i in range(2,j):
        if j%i==0:
            break
        else:
            print(j,end=" ")
