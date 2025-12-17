a= int(input("enter the number"))

try:
    print(10/a)

except Exception as err :
    print(f"Sorry an error occured due to {err}")
else:
    print("ther is no error occuring")
finally:
    print("i will run no matter what")