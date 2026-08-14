class Bank():
    """A Simple attempt to model a Bank"""

    def __init__(self, name):
        """Initialize the attirbutes for bank."""
        self.name = name
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        """Add customer into the customer list."""
        pass

    def remove_customer(self, customer):
        """Remove the given customer from the list."""
        pass

    def find_customer(self, customer_id):
        """Find the customer using the id"""
        pass

    def add_account(self, account):
        """Add account to the accounts list."""
        pass

    def remove_account(self, account):
        """Remove the given customer from the list."""
        pass

    def find_account(self, account_number):
        """Find the account using the account number."""
        pass

    def transfer_money(self, sender_account, receiver_account, amount):
        """Transfer the given ammount to the recieving account."""
        pass

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

    def deposit(self, amount):
        """Deposit the ammount in the account balance."""
        pass

    def withdraw(self, amount):
        """Withdraw the ammount give by the customer"""
        pass

    def check_balance(self):
        """Shows the current balance in the account."""
        pass

    def transfer(self):
        """Transfers the amount to the other account."""
        pass

    def show_transactions(self):
        """Displays the transactions done by the account."""
        pass

    def close_account(self):
        """Closes the account."""
        pass

class Customer():
    """Contains the information about the customer and it's accounts"""

    def __init__(self, customer_id, name, phone):
        """Initilize the customer attributes"""
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.accounts = []

    def add_account(self, account):
        """Adds the account in the customer account list."""
        pass

    def remove_account(self, account):
        """Removes the account from the customer accounts list."""
        pass

    def show_accounts(self):
        """Shows the accounts created under customer's name"""
        pass