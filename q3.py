class Bank:
    def __init__(self):
        self.accounts = {}  

    def create_account(self, customer_name, balance=0):
        if customer_name not in self.accounts:
            self.accounts[customer_name] = balance 
            print(f"Account created for {customer_name} with balance: {balance}")

    def deposit(self, customer_name, amount):
        if customer_name in self.accounts and amount > 0:
            self.accounts[customer_name] += amount  
            print(f"Deposited {amount} into {customer_name}'s account. New balance: {self.accounts[customer_name]}")

    def withdraw(self, customer_name, amount):
        if customer_name in self.accounts and 0 < amount <= self.accounts[customer_name]:
            self.accounts[customer_name] -= amount  
            print(f"Withdrew {amount} from {customer_name}'s account. Remaining balance: {self.accounts[customer_name]}")
        else:
            print(f"Insufficient funds or invalid operation for {customer_name}.")

    def get_balance(self, customer_name):
        return self.accounts.get(customer_name, "Account not found.")  

    def display_accounts(self):
        print("Current Accounts and Balances:")
        for customer, balance in self.accounts.items():
            print(f"{customer}: {balance}")

bank = Bank()
bank.create_account("Rakesh Sharma", 1000)
bank.create_account("Mukesh Verma", 500)
bank.create_account("Suresh Iyer")
bank.deposit("Rakesh Sharma", 200)
bank.withdraw("Rakesh Sharma", 150)
bank.deposit("Mukesh Verma", 300)
bank.withdraw("Mukesh Verma", 100)
bank.deposit("Suresh Iyer", 400)
bank.display_accounts()
print("Rakesh Sharma Balance:", bank.get_balance("Rakesh Sharma"))
print("Mukesh Verma Balance:", bank.get_balance("Mukesh Verma"))
print("Suresh Iyer Balance:", bank.get_balance("Suresh Iyer"))