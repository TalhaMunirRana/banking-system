class Bank():
    """A Simple attempt to model a Bank"""

    def __init__(self, name):
        """Initialize the attirbutes for bank."""
        self.name = name
        self.customers = []
        self.accounts = []

    def __str__(self):
            return f"{self.name.title()}"

    def add_customer(self, customer):
        """Add customer into the customer list."""
        self.customers.append(customer)

    def remove_customer(self):
        """Remove the given customer from the list."""
        pass

    def find_customer(self):
        """Find the customer using the id"""
        pass

    def add_account(self, account):
        """Add account to the accounts list."""
        self.accounts.append(account)

    def remove_account(self):
        """Remove the given customer from the list."""
        pass

    def find_account(self):
        """Find the account using the account number."""
        pass

    def transfer_money(self):
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

    def __str__(self):
        return f"{self.account_number} | {self.account_type} | ${self.balance}"

    def deposit(self):
        """Deposit the ammount in the account balance."""
        pass

    def withdraw(self):
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

    def __str__(self):
        return f"{self.customer_id} | {self.name.title()} | {self.phone}"

    def add_account(self):
        """Adds the account in the customer account list."""
        pass

    def remove_account(self):
        """Removes the account from the customer accounts list."""
        pass

    def show_accounts(self):
        """Shows the accounts created under customer's name"""
        pass


bank = Bank("Commercial Bank")

alan_tyler = Customer("C001", "Alan Tyler", "+12345678")

alan_tyler_account = Account("A001", alan_tyler, 1000, "1234", "Current", "Active")

bank.add_customer(alan_tyler)
bank.add_account(alan_tyler_account)
print(bank.accounts)
