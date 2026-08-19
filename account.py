class Account():
    """Model the account"""

    def __init__(self, account_number, account_holder, balance, pin, account_type, status):
        """Initialize the attributes for the account"""
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.pin = pin
        self.account_type = account_type
        self.transaction_history = []
        self.status = status

    def __str__(self):
        return f"{self.account_number} | {self.account_type} | ${self.balance}"

    def deposit(self, amount):
        """Deposit the ammount in the account balance."""
        if self.status == 'active':
            if amount > 0:
                self.balance += amount
                print(f"${amount} has been deposited.")
                self.transaction_history.append(f"Deposit - ${amount}")
            elif amount == 0:
                print("You can't deposit $0.")
            else:
                print("You can't deposit a negative amount.")
        else:
            print("You can't deposit in a closed account.")

    def withdraw(self, amount):
        """Withdraw the ammount give by the customer"""
        if self.status == 'active':
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"${amount} has been withdrawn.")
                self.transaction_history.append(f"Withdraw - ${amount}")
            elif amount == 0:
                print("You can't withdraw $0.")
            elif amount > self.balance:
                print("Insufficient funds.")
            else:
                print("You can't withdraw negative amount.")
        else:
            print("You can't withdraw from a closed account.")

    def check_balance(self):
        """Shows the current balance in the account."""
        print(f"Current balance: ${self.balance}")

    def show_transactions(self):
        """Displays the transactions done by the account."""
        print("\n---Transactions History---")
        for transaction in self.transaction_history:
            print(transaction)

    def close_account(self):
        """Closes the account."""
        self.status = 'closed'