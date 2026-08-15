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

    def find_customer(self, c_id):
        """Find the customer using the id"""
        for customer in self.customers:
            if customer.customer_id == c_id:
                print(customer)
            else:
                print("Customer does not exist.")
                break

    def add_account(self, account):
        """Add account to the accounts list."""
        self.accounts.append(account)

    def remove_account(self):
        """Remove the given customer from the list."""
        pass

    def find_account(self, acc_id):
        """Find the account using the account number."""
        for account in self.accounts:
            if account.account_number == acc_id:
                print(account)
            else:
                print("Account does not exist.")
                break

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

    def deposit(self, amount):
        """Deposit the ammount in the account balance."""
        if amount > 0:
            self.balance += amount
            print(f"${amount} has been deposited.")
            self.transaction_history.append(f"Deposit - ${amount}")
        elif amount == 0:
            print("You can't deposit $0.")
        else:
            print("You can't deposit a negative amount.")

    def withdraw(self, amount):
        """Withdraw the ammount give by the customer"""
        self.balance -= amount
        self.transaction_history.append(f"Withdraw - ${amount}")

    def check_balance(self):
        """Shows the current balance in the account."""
        print(f"Current balance: ${self.balance}")

    def transfer(self):
        """Transfers the amount to the other account."""
        pass

    def show_transactions(self):
        """Displays the transactions done by the account."""
        print("\n---Transactions History---")
        for transaction in self.transaction_history:
            print(transaction)

    def close_account(self):
        """Closes the account."""
        self.status = 'Closed'

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
        self.accounts.append(account)

    def remove_account(self):
        """Removes the account from the customer accounts list."""
        pass

    def show_accounts(self):
        """Shows the accounts created under customer's name"""
        for account in self.accounts:
            print(account)


bank = Bank("Commercial Bank")

alan_tyler = Customer("C001", "Alan Tyler", "+12345678")

alan_tyler_account = Account("A001", alan_tyler, 1000, "1234", "Current", "Active")

bank.add_customer(alan_tyler)
bank.add_account(alan_tyler_account)

alan_tyler.add_account(alan_tyler_account)

alan_tyler_account.deposit(100)
alan_tyler_account.deposit(0)
alan_tyler_account.deposit(-299)

print(alan_tyler_account.balance)




