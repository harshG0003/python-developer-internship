
def check_balance(balance):
    print("Your balance is:", balance)

def deposit(balance):
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance += amount
        print("Deposit successful.")
    else:
        print("Enter a valid amount.")
    return balance

def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Withdrawal successful.")
    return balance

pin = "1234"
balance = 1000
entered_pin = input("Enter your PIN: ")
if entered_pin == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option.")
else:
    print("Incorrect PIN.")
