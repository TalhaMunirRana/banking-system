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
        if self.customers:
            for bank_customer in self.customers:
                if customer.customer_id == bank_customer.customer_id:
                    print("Customer already exists.")
                    return
        
        self.customers.append(customer)
        print(f"Customer {customer.name.title()} added successfully")

    def remove_customer(self, c_id):
        """Remove the given customer from the list."""
        for customer in self.customers:
            if customer.customer_id == c_id:
                self.customers.remove(customer)
                break
        else:
            print("Customer does not exist.")

    def find_customer(self, c_id):
        """Find the customer using the id"""
        for customer in self.customers:
            if customer.customer_id == c_id:
                return customer
        return None

    def add_account(self, account):
        """Add account to the accounts list."""
        if account in self.accounts:
            print("Account already exists.")
            return

        customer = account.account_holder

        if customer not in self.customers:
            print("Account holder is not a customer of this bank.")
            return

        self.accounts.append(account)
        customer.add_account(account)
        print("Account created successfully.")

    def remove_account(self, acc_number):
        """Remove the given customer from the list."""
        for account in self.accounts:
            if account.account_number == acc_number:
                self.accounts.remove(account)
                break
        else:
            print("Account doesn't exist.")

    def find_account(self, acc_id):
        """Find the account using the account number."""
        for account in self.accounts:
            if account.account_number == acc_id:
                return account
        return None

    def transfer_money(self, sender_account, receiver_account, amount):
        """Transfer the given amount to the receiving account."""
        if sender_account.status == 'active' and receiver_account.status == 'active':
            if 0 < amount <= sender_account.balance:
                sender_account.balance -= amount
                sender_account.transaction_history.append(f"Sent - ${amount}")
                receiver_account.balance += amount
                receiver_account.transaction_history.append(f"Received - ${amount}")
            elif amount == 0:
                print("You can't transfer $0")
            elif amount > sender_account.balance:
                print("Insufficient funds")
            else:
                print("You can't transfer a negative amount.")
        else:
            print("You can't transfer to and from closed accounts.")