class BankAccount:
    def __init__(self, name, account_num, initial_checking, initial_savings):
        self.name = name
        self.account_num = account_num
        self.checking = initial_checking
        self.savings = initial_savings

    def deposit_checking(self, amount):
        self.checking += amount

    def deposit_savings(self, amount):
        self.savings += amount

    def withdraw_checking(self, amount):
        self.checking -= amount 
    
    def withdraw_savings(self, amount):
        self.savings -= amount
    
my_account = BankAccount('Code Dog', 125924, 200, 200)

class Bank:
    def __init__(self, initial_accounts = []):
        """Create bank starting with list of accounts initial_accounts."""
        self.accounts = initial_accounts
    
    def create_account(self, account):
        self.accounts.append(account)

    def close_account(self, account):
        self.accounts.remove(account)
    
    def get_account_by_name(self, name):
        for account in self.accounts:
            if name == account.name:
                return account
        print('could not find an account with that name.')

    
    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if account.account_num == account_number:
                return account 
        print('could not find an account with that number.')


code_dog_credit_union = Bank()

print('Welcome to the Code Dog Credit Union!')

done = False

def open_account():
    pass 

def close_account():
    pass 

def access_account():
    pass


while not done:
    print('1 - Open an account')
    print('2 - Close an account')
    print('3 - Access my account')
    print('4 - Exit')
    print()
    choice = input('choose an option: ')
    print()

    if choice == '1':
        open_account()
    elif choice == '2':
        close_account() 
    elif choice == '3':
        access_account() 
    elif choice == '4':
        done = True
    else: 
        print('Not a valid menu option')

