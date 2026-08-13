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
        self.accounts.append(account)

    def remove_account(self, account):
        """Removes the account from the customer accounts list."""
        self.accounts.remove(account)

    def show_accounts(self):
        """Shows the accounts created under customer's name"""
        for account in self.accounts:
            print(f"{account.account_number}: {account.account_type}")