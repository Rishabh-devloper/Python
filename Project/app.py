import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(page_title="Bank Management System", layout="centered")
st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Delete Account"
    ]
)

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        success, result = bank.create_account(
            name, age, email, int(pin)
        )
        if success:
            st.success("Account Created Successfully!")
            st.write(result)
        else:
            st.error(result)

# ---------------- DEPOSIT ----------------
elif menu == "Deposit Money":
    st.subheader("Deposit Money")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, msg = bank.deposit(acc_no, int(pin), amount)
        if success:
            st.success(f"New Balance: ₹{msg}")
        else:
            st.error(msg)

# ---------------- WITHDRAW ----------------
elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, msg = bank.withdraw(acc_no, int(pin), amount)
        if success:
            st.success(f"Remaining Balance: ₹{msg}")
        else:
            st.error(msg)

# ---------------- SHOW DETAILS ----------------
elif menu == "Show Details":
    st.subheader("Account Details")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = bank.find_user(acc_no, int(pin))
        if user:
            st.json(user)
        else:
            st.error("Invalid Credentials")

# ---------------- DELETE ACCOUNT ----------------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        if bank.delete_account(acc_no, int(pin)):
            st.success("Account Deleted Successfully")
        else:
            st.error("Invalid Credentials")
