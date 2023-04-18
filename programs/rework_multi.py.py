import random
class User_deposit:
    def account_number_validation(self):
        while True:
            try:
                account_number=random.randrange(10000,100000)
                return account_number
            except:
                print('Enter account number')
    def account_balance_validation(self):
        while True:
            try:
                account_balance=int(input('Enter Account balance: '))
                return account_balance
            except:
                print('Enter valid account balance')
class User_borrow:
    def loan_number_validation(self):
        while True:
            try:
                loan_number=random.randrange(1000,10000)
                return loan_number
            except:
                print('Enter valid loan number')
    def loan_amount_validation(self):
        while True:
            try:
                loan_amount=int(input('Enter Loan amount: '))
                return loan_amount
            except:
                print('Enter valid loan amount')
class User_account(User_borrow,User_deposit):
    details={}
    def __init__(self):
        while True:
            try:
                self.name=input('Enter Name: ')
                if self.name.isalpha() and len(self.name)>0:
                    break
                else:
                    raise BaseException
            except:
                print('Enter valid name')
        while True:
            try:
                self.number=input('Enter Phone-number: ')
                if self.number.isnumeric() and len(self.number)==10:
                    break
                else:
                    raise BaseException
            except:
                print('Enter valid number')
    def add_details(self):
        customer_ac_number=self.account_number_validation()
        customer_balance=self.account_balance_validation()
        custmer_loan_number=self.loan_number_validation()
        customer_loan_amount=self.loan_amount_validation()
        User_account.details.update([(customer_ac_number,[self.name,self.number,customer_balance,custmer_loan_number,customer_loan_amount])])
    def customer_full_details(self):
        for i,j in User_account.details.items():
            print('Details of Customer')
            print('------------------------------------------------------')
            print(f'Customer Name: {j[0]}')
            print(f'Ph no is {j[1]} , Customer A/c number {i} and Balance {j[2]}')
            print('------------------------------------------------------')
            print(f'Loan number is {j[3]} and loan amount is {j[4]}')

no_of_user=int(input('Enter number of customer details you want to add : '))
count=0
while count<no_of_user:
    customer1=User_account()
    customer1.add_details()
    count=count+1
customer1.customer_full_details()

















