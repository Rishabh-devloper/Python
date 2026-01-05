import json
import random
import string
from pathlib import Path

DB_PATH = Path("data.json")


class Bank:
    def __init__(self):
        if DB_PATH.exists():
            with open(DB_PATH, "r") as f:
                self.data = json.load(f)
        else:
            self.data = []

    def save(self):
        with open(DB_PATH, "w") as f:
            json.dump(self.data, f, indent=4)

    def generate_account_no(self):
        return "".join(
            random.sample(
                string.ascii_letters + string.digits + "!@#$%^&*", 7
            )
        )

    def find_user(self, acc_no, pin):
        for user in self.data:
            if user["account_no"] == acc_no and user["pin"] == pin:
                return user
        return None

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Age must be ≥18 and PIN must be 4 digits"

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_no": self.generate_account_no(),
            "balance": 0
        }

        self.data.append(user)
        self.save()
        return True, user

    def deposit(self, acc_no, pin, amount):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        if amount <= 0 or amount > 10000:
            return False, "Invalid amount"

        user["balance"] += amount
        self.save()
        return True, user["balance"]

    def withdraw(self, acc_no, pin, amount):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        if amount > user["balance"]:
            return False, "Insufficient balance"

        user["balance"] -= amount
        self.save()
        return True, user["balance"]

    def delete_account(self, acc_no, pin):
        user = self.find_user(acc_no, pin)
        if not user:
            return False

        self.data.remove(user)
        self.save()
        return True
