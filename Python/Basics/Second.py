#factorial of a number

# a= int(input("enrter the no"))
# fact = 1
# for i in range (1,a+1,1):
#     fact= fact * i
# print(fact)

"""                                                   perfect number                       """
# num = int(input("enter the number"))

# sum1 = 0 

# for i in range(1,num):
#     if num % i==0:
#         sum1 = sum1+i
# print(sum1)
# if num == sum1 :
#     print(f"{num} is a perfect number")

"""                                                     prime number                                            """
# 




"""                                                     reverse string                                                            """
# str = input("enter the striung")
# rev= " "
# for i in range(len(str)-1,-1,-1):
#     rev = rev + str[i]
# print(rev)


""" Palindrome in string"""
# str = input("enter the striung")
# rev= ""
# for i in range(len(str)-1,-1,-1):
#     rev = rev + str[i]
# print(rev)
# if str == rev:
#     print("it is palindrome")
# else:
#     print("it is not palindrom")
"""count letter chatacyers and alphbets"""

str =input("enter the string : ")
dig = 0 
alpha=0
speci =0
for i in str:
    if i.isdigit():
        dig +=1 ;
    elif i.isalpha():
        alpha+=1
    else:
        speci+=1
print(f"number of digits are {dig}\n number of alphabets are {alpha}\n number of special characxter are{speci}")