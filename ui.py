# Import the banking module to access banking functions
import banking

# Function to display the main menu of the bank system
def main_menu():
    # Display the main options for the user to choose from
    print("Welcome to Python Bank!")
    print("1. Create Account")
    print("2. Modify Account")
    print("3. Close Account")
    print("4. Check Balance")
    print("5. Deposit")
    print("6. Withdraw")
    print("0. Exit")

# Function to run the banking system
def run():
    # Start a loop to continuously show the menu and process user input
    while True:
        # Show the main menu
        main_menu()
        # Ask the user to choose an option
        choice = input("Choose an option: ")

        # If the user chooses option 1 create a new account
        if choice == "1":
            # Ask for account ID and name
            acc = input("Enter Account ID: ")
            name = input("Enter Name: ")
            # Call create_account function from banking module
            print(banking.create_account(acc, name))
        # If the user chooses option 2 modify an existing account
        elif choice == "2":
            # Ask for account ID and new name
