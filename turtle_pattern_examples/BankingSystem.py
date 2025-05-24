
#  create an BankAccount class with the following attributes:


class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:  # check if amount is positive and less than or equal to balance
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        print(f"Current balance: ₹{self.balance}")


def main():
    print("Welcome to the Simple Banking System")
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")

    account = BankAccount(account_number, account_holder)  # create a BankAccount object
    print("\nAccount created successfully!")

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '3':
            account.get_balance()
        elif choice == '4':
            print("Thank you !")
            break
        else:
            print("Invalid choice. Please try again.")


main()
