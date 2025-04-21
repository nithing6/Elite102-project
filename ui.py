import banking

def main_menu():
    print("Welcome to Python Bank!")
    print("1. Create Account")
    print("2. Modify Account")
    print("3. Close Account")
    print("4. Check Balance")
    print("5. Deposit")
    print("6. Withdraw")
    print("0. Exit")

def run():
    while True:
        main_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            acc = input("Enter Account ID: ")
            name = input("Enter Name: ")
            print(banking.create_account(acc, name))
        elif choice == "2":
            acc = input("Enter Account ID: ")
            name = input("Enter New Name: ")
            print(banking.modify_account(acc, name))
        elif choice == "3":
            acc = input("Enter Account ID: ")
            print(banking.close_account(acc))
        elif choice == "4":
            acc = input("Enter Account ID: ")
            print(f"Balance: ${banking.check_balance(acc)}")
        elif choice == "5":
            acc = input("Enter Account ID: ")
            amount = float(input("Enter Amount: "))
            print(banking.deposit(acc, amount))
        elif choice == "6":
            acc = input("Enter Account ID: ")
            amount = float(input("Enter Amount: "))
            print(banking.withdraw(acc, amount))
        elif choice == "0":
            print("Thank you for using Python Bank!")
            break
        else:
            print("Invalid choice. Try again.")
