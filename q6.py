class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient balance for withdrawal.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")


if __name__ == "__main__":
    account = BankAccount("4685-3251-6662-0271", 1200)
    print("Initial Account Details:")
    account.display_details()

    account.deposit(500)
    account.withdraw(200)
    print("\nUpdated Account Details:")
    account.display_details()
