class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print (f"Deposited : ${amount}.\nNew balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print (f"Withdrown : ${amount}.\nNew balance: ${self.balance}.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")

    def send_money(self, amount, account_number):
        if account_number != self.account_number:
            if amount > 0:
                self.balance -= amount
                print(f"You sent ${amount} to {account_number}")
                return amount, account_number
            else:
                print("Amount must be greater than 0")
        else:
            print("You can't send money to yourself")

    def receive_money(self, amount):
        self.balance += amount


class Bank:
    account_database = []

    def add_account(self):
        account_holder = input("Write holder's name: ")
        account_number = int(len(self.account_database) + 1)
        account = BankAccount(account_number, account_holder)
        self.account_database.append(account)
        print (f"Successful! account n°{account_number} created for {account_holder}")
        q = input("Press any key to return to menu")


Intesa = Bank()

def ATM():
    while True:
        print("------------------------------------------")
        print()
        print("1. Add Account")
        print("2. View account information")
        print("3. Transfer money")
        print("4. Deposit money")
        print("5. Withdraw money")
        print("q to close the app")
        print()
        print("------------------------------------------")
        print()
        choice = input("Choose an action: ").lower().strip()
        match choice:
            case "1":
                Intesa.add_account()
                
            case "2":
                account_num = int(input("Which account number's do you want to view? ").strip())
                for account in Intesa.account_database:
                    if account.account_number != account_num:
                        continue
                    else:
                        print(f"Account holder's Name: {account.account_holder}")
                        print(f"Total balance: ${account.balance}")
                        q = input("Press any key to return to menu")
            case "3":
                sender_num = int(input("From which account number do you send: ").strip())
                receiver_num = int(input("Which account number will receive the money: ").strip())
                amnt = int(input("How much $ do you want to send? ").strip())
                for account in Intesa.account_database:
                    if account.account_number != sender_num:
                        continue
                    else:
                        account.send_money(amnt, receiver_num)
                for account in Intesa.account_database:
                    if account.account_number != receiver_num:
                        continue
                    else:
                        account.receive_money(amnt)
                print(f"Successful! account n°{sender_num} sent ${amnt} to account n°{receiver_num}")
                q = input("Press any key to return to menu")
            case "4":
                account_num = int(input("write a valid account number to deposit: ").strip())
                amnt = int(input("How much $ do you want to Deposit? ").strip())
                for account in Intesa.account_database:
                    if account.account_number != account_num:
                        continue
                    else:
                        account.deposit(amnt)
                        print(f"Successful! ${amnt} deposited on account n°{account_num}")
                        q = input("Press any key to return to menu")
            case "5":
                account_num = int(input("write a valid account number to withdraw: ").strip())
                amnt = int(input("How much $ do you want to Withdraw? ").strip())
                for account in Intesa.account_database:
                    if account.account_number != account_num:
                        continue
                    else:
                        account.withdraw(amnt)
                        print(f"Successful! ${amnt} withdrawn from account n°{account_num}")
                        q = input("Press any key to return to menu")
            case "q":
                print("Thank you! See you soon.")
                break

def main():
    ATM()

print("Welcome to bank system simulator")
main()