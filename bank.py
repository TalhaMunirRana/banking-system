class Bank():
    """A Simple attempt to model a Bank"""

    def __init__(self, name):
        """Initialize the attirbutes for bank."""
        self.name = name
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        """Add customer into the customer list."""
        self.customers.append(customer)

    def remove_customer(self, customer):
        """Remove the given customer from the list."""
        self.customers.remove(customer)

    def find_customer(self, customer_id):
        """Find the customer using the id"""
        if customer_id in self.customers:
            print(self.customers[customer_id])

    def add_account(self, account):
        """Add account to the accounts list."""
        self.accounts.append(account)

    def remove_account(self, account):
        """Remove the given customer from the list."""
        self.accounts.remove(account)

    def find_account(self, account_number):
        """Find the account using the account number."""
        if account_number in self.accounts:
            print(self.accounts[account_number])

    def transfer_money(self, sender_account, receiver_account, amount):
        """Transfer the given ammount to the recieving account."""
        pass