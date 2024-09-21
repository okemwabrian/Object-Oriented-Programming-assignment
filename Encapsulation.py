class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.__account_holder = account_holder  # Private variable
        self.__balance = initial_balance  # Private variable
    
    # Getter method for account_holder (public)
    def get_account_holder(self):
        return self.__account_holder

    # Getter method for balance (public)
    def get_balance(self):
        return self.__balance
    
    # Setter method to deposit money (public)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
    
    # Setter method to withdraw money (public)
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

# Creating an instance of BankAccount
account = BankAccount("Okemwa Brian", 5000)

# Accessing the private attributes using public methods
print("Account Holder:", account.get_account_holder())
print("Current Balance:", account.get_balance())

# Modifying the balance using public methods
account.deposit(1000)
account.withdraw(2000)
print("Updated Balance:", account.get_balance())
