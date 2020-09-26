#add,sub,mul,div
import math
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input('Enter a value:-'))
b=int(input('Enter b value:-'))
c=int(input('Enter a choice:-'))
if c==1:
    print(add(a,b))
elif c==2:
    print(sub(a,b))
elif c==3:
    print(mul(a,b))
elif c==4:
    print(div(a,b))
else:
    exit






