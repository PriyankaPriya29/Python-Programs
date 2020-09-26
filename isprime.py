from math import sqrt
n=int(input('Enter a number:-'))
def is_prime(n):
    s=int(sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
def right_prime(n):
    i=n+1
    while 1:
        if is_prime(i):
            return i
        i+=1
print(right_prime(n))
def left_prime(n):
    j=n-1
    while 1:
        if is_prime(j):
            return j
    j=j-1
    print(left_prime(n))
def near_prime(n):
    if is_prime(n):
        return n
    else:
        x=right_prime(n)
        y=left_prime(n)
        if abs(n-x)<abs(n-y):
            print(x)
        elif abs(n-x)>abs(n-y):
            print(y)
        else:
            print(x,y)
near_prime(n)
