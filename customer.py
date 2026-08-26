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

    def add_account(self, account):
        """Adds the account in the customer account list."""
        if account not in self.accounts:
            self.accounts.append(account)
        else:
            print("Account already exists.")

    def remove_account(self, acc_number):
        """Removes the account from the customer accounts list."""
        for account in self.accounts:
            if account.account_number == acc_number:
                self.accounts.remove(account)
                break
        else:
            print("Account doesn't exist.")

    def show_accounts(self):
        """Shows the accounts created under customer's name"""
        for account in self.accounts:
            print(f"\nAccount Number: {account.account_number}")
            print(f"Account Holder: {account.account_holder.name.title()}")
            print(f"Account Type: {account.account_type}")
            print(f"Balance: ${account.balance}")
            print(f"Status: {account.status}")