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

