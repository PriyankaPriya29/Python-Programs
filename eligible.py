n=int(input('Enter your percentage:'))
m=int(input('Enter your arrears:'))
if (n>60 and m == 0):
    print ('student eligible')
elif  (n<60 and m>0):
    print ('student not eligible')
else:
    print('Rejected')
    
   
