nterms = int(input("Number of terms:"))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)            
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
    

#xact num
       for i in range(3,n+1)
       s=a+b
       a=b
       b=s
       print(b)




#nearst fibonacci
n=int(input('Enter a range:-'))
a=0
b=1
for i in range(3,n+1):
   p=a+b
   a=b
   b=p
   if b>=n:
      print(a)
      break
