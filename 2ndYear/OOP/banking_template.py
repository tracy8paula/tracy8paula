class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount is too low!")
            return
        
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount:.2f}")
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account holder: {self.account_holder_name}")
        print(f"Account balance: ${self.balance:.2f}")

    def apply_interest(self, rate):
        interest_amount = self.balance * rate
        self.balance += interest_amount
        self.transaction_history.append(f"Interest applied: ${interest_amount:.2f} (rate: {rate*100:.1f}%)")
        print(f"Interest of ${interest_amount:.2f} applied. New balance: ${self.balance:.2f}")

    def show_transaction_history(self):
        print(f"\nTransaction History for {self.account_holder_name} (Account: {self.account_number})")
        if not self.transaction_history:
            print("No transactions found.")
        else:
            for i, transaction in enumerate(self.transaction_history, 1):
                print(f"{i}. {transaction}")

    def transfer_to(self, receiver_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            receiver_account.balance += amount
            
            # Record transaction in both accounts' histories
            self.transaction_history.append(f"Transferred ${amount:.2f} to account {receiver_account.account_number}")
            receiver_account.transaction_history.append(f"Received ${amount:.2f} from account {self.account_number}")
            
            print(f"Successfully transferred ${amount:.2f} from {self.account_number} to {receiver_account.account_number}")
            print(f"Your new balance: ${self.balance:.2f}")
            return True
        else:
            print("Insufficient funds for transfer.")
            return False

accounts = {} 

while True:
    print(" BANKING SYSTEM MENU")
    print("="*25)
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Apply Interest")
    print("6. Show Transaction History")
    print("7. Transfer Funds")
    print("8. Exit")
    print("="*25)

    choice = input("Choose an option: ")

    if choice == '1':
        account_number = input("Enter new account number: ")
        if account_number in accounts:
            print("Account number already exists. Please choose a different number.")
            continue
        
        account_holder_name = input("Enter account holder's name: ")
        try:
            initial_balance = float(input("Enter initial balance: "))
            if initial_balance < 0:
                print("Initial balance cannot be negative.")
                continue
        except ValueError:
            print("Invalid balance amount. Please enter a number.")
            continue
            
        accounts[account_number] = BankAccount(account_number, account_holder_name, initial_balance)
        print(f"Account created successfully for {account_holder_name}.")
        
    elif choice == '2':
        account_number = input("Enter account number: ")
        if account_number not in accounts:
            print("Account not found.")
            continue
            
        try:
            amount = float(input("Enter amount to deposit: "))
            accounts[account_number].deposit(amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            
    elif choice == '3':
        account_number = input("Enter account number: ")
        if account_number not in accounts:
            print("Account not found.")
            continue
            
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount < 0:
                print("Withdrawal amount cannot be negative.")
                continue
            accounts[account_number].withdraw(amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            
    elif choice == '4':
        account_number = input("Enter account number: ")
        if account_number not in accounts:
            print("Account not found.")
            continue
        accounts[account_number].check_balance()
        
    elif choice == '5':
        account_number = input("Enter account number: ")
        if account_number not in accounts:
            print("Account not found.")
            continue
            
        try:
            rate = float(input("Enter interest rate (e.g., 0.05 for 5%): "))
            if rate < 0:
                print("Interest rate cannot be negative.")
                continue
            accounts[account_number].apply_interest(rate)
        except ValueError:
            print("Invalid interest rate. Please enter a number.")
            
    elif choice == '6':
        account_number = input("Enter account number: ")
        if account_number not in accounts:
            print("Account not found.")
            continue
        accounts[account_number].show_transaction_history()
        
    elif choice == '7':
        source_account = input("Enter source account number: ")
        if source_account not in accounts:
            print("Source account not found.")
            continue
            
        receiver_account = input("Enter receiver account number: ")
        if receiver_account not in accounts:
            print("Receiver account not found.")
            continue
            
        if source_account == receiver_account:
            print("Cannot transfer to the same account.")
            continue
            
        try:
            amount = float(input("Enter amount to transfer: "))
            if amount <= 0:
                print("Transfer amount must be positive.")
                continue
            accounts[source_account].transfer_to(accounts[receiver_account], amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            
    elif choice == '8':
        print("Thank you for using the Banking System. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select a number from 1-8.")