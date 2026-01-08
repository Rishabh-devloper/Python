"""                                                           WHILE LOOP                                                                                                                       """

#rev number

n = int(input("enter the number "))

rev= 0
temp=n
while n>0:
    rev = rev*10 +n%10;
    n=n //10 
print(rev)
if temp == rev :
    print("it is palindrome number")
else:
    print("not palindroem")
