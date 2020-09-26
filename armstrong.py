n=int(input('Enter a number:'))
s=0
a=n
while n>0:
    rem*n%10
    print(rem,'is the rminder value)
    s+=rem*rem*rem
    print(s,'is the s value')
    n=n//10
    if a==s:
        print(a,'is an armstrong..')
        else:
            print(a,'is not an armstrong number..')
