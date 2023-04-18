class My_account:
    count_of_account_holder=0
    amount_patable_by_bank=0
    def __init__(self,account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    def account_detail(self):
        print(f'Account Number: {self.account_number}')
        print(f'Account Holder Name: {self.name}')
        print(f'Current Balance: {self.balance}')
    def deposit(self,deposit_amount):
        print(f'{deposit_amount} is successfully added.')
        self.balance=self.balance+deposit_amount
        print(f'Available balance is {self.balance}')
    @classmethod
    def simple_interest(cls,amount,year,interest):
        My_account.amount_patable_by_bank=(amount*year*interest)/100
        My_account.count_of_account_holder=My_account.count_of_account_holder+1
        print('Numbern of accounts in our bank is {My_account.count_of_account_holder}')
    @classmethod
    def bank_payable(cls):
        print(f'Bank payable amount is ')
    def withdrawal(self,withdrawal_amount):
        print(f'{withdrawal_amount} is successfully withdrawn.')
        self.balance=self.balance-withdrawal_amount
        print(f'Available balance is {self.balance}')
while True:
    try:
        acc_number=int(input('Enter 5-digit Account number of account holder: '))
    except:
        print('Enter valid account number')
    else:
        try:
            if len(str(acc_number))==5:
                break
            else:
                raise BaseException
        except:
            print('Enter valid account number')

while True:
    try:
        enter_name=input('Name of the account holder in a bank: ')
        if enter_name.isalpha() and len(enter_name)>0:
            break
        else:
            raise BaseException
    except:
        print('Enter valid name')
while True:
    try:
        acc_balance=int(input('Enter balance amount in your account: '))
        break
    except:
        print('Enter valid amount')
user_account=My_account(acc_number,enter_name,acc_balance)
user_account.account_detail()
user=My_account(acc_number,enter_name,acc_balance)
user.account_detail()
interset_amount=float(input("Enter the principal amount : "))
no_of_year=float(input("Enter the number of years : "))
rate_of_interest=float(input("Enter the rate of interest : "))
user_account.simple_interest(interset_amount,no_of_year,rate_of_interest)
