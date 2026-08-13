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
        print(f"{self.account_number}: {self.account_type}")

    def deposit(self, amount):
        """Deposit the ammount in the account balance."""
        if amount > 0:
            self.balance += amount
        elif amount == 0:
            print(f"You can't deposit ${amount}.")
        else:
            print(f"You can't deposit negative amount.")

    def withdraw(self, amount):
        """Withdraw the ammount give by the customer"""
        if 0 < amount <= self.balance: 
            self.balance -= amount
        elif amount > self.balance:
            print("Insufficient funds.")
        elif amount == 0:
            print("You can't withdraw $0.")
        else:
            print("You can't withdraw negative amount.")

    def check_balance(self):
        """Shows the current balance in the account."""
        print(f"Your balance is: {self.balance}")

    def transfer(self):
        """Transfers the amount to the other account."""
        pass

    def show_transactions(self):
        """Displays the transactions done by the account."""
        for transaction in self.transaction_history:
            print(transaction)

    def close_account(self):
        """Closes the account."""
        if self.status == 'active':
            self.status == 'closed'
            print("Your account has been closed.")
        elif self.status == 'closed':
            print("Your account is already closed.")
        