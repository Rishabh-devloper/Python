import json
import random
import string
from pathlib import Path


class Bank():
    database = 'BANK MANAGEMENT\data.json'
    data=[]

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
       print(f"an exception occur as {err}")

    @staticmethod
    def __update():
        with open(Bank.database,'w')as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountGenrate(cls):
        alpha = random.choices(string.ascii_letters, k =3 )
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
    
    def CreateAccount(self):

        data = {
            "name":input("tell your name :- "),
            "age":int(input("tell your age :- ")),
            "email":input("tell your email :- "),
            "pin": int(input("tell us your pin :- " )),
            "accounNo": Bank.__accountGenrate(),
            "Balance": 0
        }
        if data["age"]<18 or len(str(data["pin"])) != 4:
            print("sorry you cannot create your account ")
        else:
            print("Account Created Sucessfully ")
            for i in data:
                print(f"{i}: {data[i]}")
            print("Please! Note down your account number ")
            Bank.data.append(data)
            Bank.__update()

    def DepositMoney(self):
        accNum=input("please tell your account number")
        pin = int(input("please tell your pin"))
        userdata = [i for i in Bank.data if i['accounNo']== accNum and i["pin"]== pin]

        if userdata == False:
            print("sorry no dat found")
        else:
            amount = int(input("how much you want to deposit"))
            if amount>10000 or amount <0:
                print("sorry the amount is too much . you can deposit below 10000")
            else:
                userdata[0]['Balance']+= amount
                Bank.__update()
                print("Amount deposited  succesfully")
    def WithdrawMoney(self):

        accNum=input("please tell your account number")
        pin = int(input("please tell your pin"))
        userdata = [i for i in Bank.data if i['accounNo']== accNum and i["pin"]== pin]

        if userdata == False:
            print("sorry no data found")
        else:
            amount = int(input("how much you want to withdraw"))
            if userdata[0]['Balance'] < amount:
                print("Sorry u dont have that much money ")
            else:
                userdata[0]['Balance']-= amount
                Bank.__update()
                print("Amount Withdrwaed succesfully")
    def ShowDetails(self):
        accNum=input("please tell your account number")
        pin = int(input("please tell your pin"))

        userdata= [i for i in Bank.data if i['accounNo']== accNum and i["pin"]== pin]
        print("print Your information \n\n\n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")
    def UpdateDetails(self):
        accNum=input("please tell your account number")
        pin = int(input("please tell your pin"))
        userdata = [i for i in Bank.data if i['accounNo']== accNum and i["pin"]== pin]

        if userdata == False:
            print("No such User Found")
        else:
            print("U can not change the age ,  account number and balance")

            print("Fill the details for the chyange or leave it empty")

            newData={
                "name":input("Please tell new name or press enter :- "),
                "email":input("please tell your new email or press enter to skip :- "),
                "pin":input("Enter your new pin or enter to skip :- ")
            }
            if newData["name"] == "":
                newData["name"]= userdata[0]['name']
            if newData["email"] == "":
                newData["email"]= userdata[0]['email']
            if newData["pin"] == "":
                newData["pin"]= userdata[0]['pin']
            
            newData['age'] = userdata[0]['age']
            newData['accounNo'] = userdata[0]['accounNo']
            newData['Balance'] = userdata[0]['Balance']

            if type(newData['pin'])== str:
                newData['pin'] = int(newData['pin']) 
            
            for i in newData:
                if newData[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newData[i]
            Bank.__update()
            print("Bank Details updated Sucessfully")
    def DeleteUser(self):
        accNum=input("please tell your account number")
        pin = int(input("please tell your pin"))
        userdata = [i for i in Bank.data if i['accounNo']== accNum and i["pin"]== pin]

        if userdata == False:
            print("No such data found")
        else:
            check = input("Enter Y or y if u actually want to delete the account or press n for cnacel")
            if check== 'n' or check=='N':
                pass
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted SuccessFully")
                Bank.__update()





user = Bank()

print("Press 1 for Creating an account ")
print("Press 2 for Depositing the Money ")
print("Press 3 for Withdrawing the Money ")
print("Press 4 for details  ")
print("Press 5 for updating the details ")
print("Press 6 for Deleteing Ur account")

check = int(input("tell your resaponse :- "))

if check== 1:
    user.CreateAccount()
if check == 2:
    user.DepositMoney()
if check == 3:
    user.WithdrawMoney()

if check ==4:
    user.ShowDetails()
if check == 5:
    user.UpdateDetails()
if check==6:
    user.DeleteUser()