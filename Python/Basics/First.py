# st='sherr'
"""Q1. Accept two numbers and print the greatest between them.
Q2. Accept the gender from the user as char and print the
respective greeting message
Ex - Good Morning Sir (on the basis of gender)
Q3. Accept an integer and check whether it is an even number
or odd.
Q4. Accept name and age from the user. Check if the user is a
valid voter or not.
Ex- “hello shery you are a valid voter”
Q5. Accept a year and check if it a leap year or not (google to
find out what is a leap year)"""

# Q1.
# num1=int(input("enter first number"))
# num2 = int(input("enter 2 number"))

# if num1<num2:
#     print(f"{num2} is greater than {num1}")
# elif num1==num2:
#     print(f"{num2} is equal to  {num1}")
# else:
#     print(f"{num1} is greater than {num2}")

# #Q2
# def Greeting(gen):
#     if gen=="male" :
#         print("good morning sir ")
#     elif gen=="female":
#         print("good morning Maam")
#     else:
#         print("enter correct gender")


# gen=input("enter the gender")
# Greeting(gen)

# Q4
# def valid (name , age):
#     if age>18 :
#         print(f"Hey {name} You are valid for vote")
#     else :
#         print(F"{name} you are valid Voter ")

# name = input("enter Your Name")
# age=int(input("enter your age"))
# valid(name , age)

# Q5 
# def leap_year (year):
#     if year % 400 == 0 :
#         print(f"{year} is leap year")
    
#     elif year %100 == 0:
#         print(f"{year} is not leap year")
#     elif year% 4 == 0 :
#         print(f"{year} is leap year")
#     else:
#         print(f"{year} is not leap year")
# year = int(input("enter year"))
# leap_year(year)

""""                            IF ELSE LADDER QUESTION                                      """

"""You cna also create if elif ladder using multiple conditions of
elif.j
@ For understanding solve this questionj
@ take the input of temperature in celsiusX
@ Below 0°C → "Freezing Cold b
@ 0°C to 10°C → "Very Cold b
@ 10°C to 20°C → "Cold b
@ 20°C to 30°C → "Pleasant b
@ 30°C to 40°C → "Hot b
@ Above 40°C → "Very Hot 

"""
def Weather(temp):
    if temp <0:
        print("Freezing Cold temprature")
    elif temp >0 and temp <10 :
        print("very Cold")
    elif temp>10 and temp<20 :
        print("Cold Weather")
    elif temp>20 and temp<30 :
        print("pleasent")
    elif temp>30 and temp<40 :
        print("Hot")
    else :
        print("Very HOT")
temp = int(input("Enter the temprature in celsius"))
Weather(temp)
