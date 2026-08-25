from bank import Bank
from account import Account
from customer import Customer


bank = Bank("Python National Bank")

while True:
    print("\n" + "=" * 37)
    print(f"{bank} - Banking System")
    print("=" * 37)

    print("""
1. Add customer
2. Create Account
3. Deposit
4. Withdraw
5. Check Balance
6. Transfer Money
7. Show Transactions
8. Show Customer Accounts
9. Find Customer
10. Find Account
11. Close Account
12. Exit
""")

    choice = input("\nEnter your choice: ")

    # Add customer
    if choice == '1':
        print("\n--- Add Customer ---")

        customer_id = input("Customer ID: ").strip()
        name = input("Customer Name: ").strip()
        phone = input('Customer Phone: ').strip()

        customer = Customer(customer_id, name, phone)
        bank.add_customer(customer)

    # Create Account
    elif choice == '2':
        print("\n--- Create Account ---")

        customer_id = input("Customer ID: ").strip()
        customer = bank.find_customer(customer_id)

        if customer is None:
            print("Customer doesn't exist.")
            continue

        account_number = input("Account Number: ").strip()

        if bank.find_account(account_number):
            print("Account already exists.")
            continue

        account_type = input("Account type (checkings/saving): ").strip().lower()
        pin = input("Set PIN: ").strip()

        try:
            balance = float(input("Initial Deposit: $"))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if balance < 0:
            print("Balance can not be a negative amount.")
            continue

        account = Account(account_number, customer, balance, pin, account_type, 'active')

        bank.add_account(account)

    # Deposit
    elif choice == '3':
        print("\n--- Deposit Amount ---")

        acc_number = input("Account Number: ").strip()
        account = bank.find_account(acc_number)

        if account is None:
            print("Account does not exists.")
            continue

        try:
            amount = float(input("Enter Deposit amount: $"))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        account.deposit(amount)

    # Withdraw
    elif choice == '4':
        print("\n--- Withdraw ---")

        acc_number = input("Account Number: ").strip()
        account = bank.find_account(acc_number)

        if account is None:
            print("Account does not exists.")
            continue

        try:
            amount = float(input("Enter withdraw amount: $"))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        account.withdraw(amount)

    # Check Balance
    elif choice == '5':
        print("\n--- Check Balance ---")

        acc_number = input("Account Number: ").strip()
        account = bank.find_account(acc_number)

        if account is None:
            print("Account does not exists.")
            continue

        account.check_balance()

    # Transfer Money
    elif choice == '6':
        print("\n--- Transfer money ---")

        sender_acc_number = input("Sender Account Number: ").strip()
        sender_account = bank.find_account(sender_acc_number)

        if sender_account is None:
            print("Sender account does not exists.")
            continue

        reciever_acc_number = input("Receiver Account Number: ").strip()
        reciever_account = bank.find_account(reciever_acc_number)

        if reciever_account is None:
            print("Reciever account does not exists.")
            continue

        try:
            amount = float(input("Enter the amount: $"))
        except ValueError:
            print("Please enter a valid amount.")

        bank.transfer_money(sender_account, reciever_account, amount)

    # Show transactions
    elif choice == '7':
        print("\n--- Transaction History ---")

        acc_number = input("Account number: ").strip()
        account = bank.find_account(acc_number)

        if account is None:
            print("Account does not exists.")
            continue

        account.show_transactions()

    # Show customer accounts
    elif choice == '8':
        print("\n--- Customer Accounts ---")

        customer_id = input("Customer ID: ").strip()
        customer = bank.find_customer(customer_id)

        if customer is None:
            print("Customer does not exists.")
            continue

        print(f"\n{customer.name.title()} Accounts:")
        customer.show_accounts()
        
    # Find customer
    # Find account
    # Close account
    # Exit
    elif choice == '12':
        break
    else:
        print("Please enter a valid option")

        

