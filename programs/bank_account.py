#reworked 18/1/23
import random
global cust_data,all_cust_data,new_user_attributes
all_cust_data={}
new_user_attributes=['name', 'address', 'phone number', 'govt id', 'amount']
def bank_account():
    cust_data={}
    while True:
        while True:
            try:
                enter_name=input('Enter Full name: ')
                if enter_name.isalpha() and len(enter_name)>0:
                    cust_data.update([('name',enter_name)])
                    break
                else:
                    raise BaseException
            except:
                print('Enter valid name')
        while True:
            try:
                enter_address=input('Enter residential address: ')
                if enter_address.isalpha() and len(enter_address)>0:
                    cust_data.update([('address',enter_address)])
                    break
                else:
                    raise BaseException
            except:
                print('Enter valid address')
        while True:
            try:
                riders_number=input('Enter personal number: ')
                if riders_number.isnumeric() and len(riders_number)==10:
                    cust_data.update([('Phone number',riders_number)])
                    break
                else:
                    raise BaseException
            except:
                print('Enter valid number')
        while True:
            try:
                accountant_id=input("Enter Goverment ID number('startwith uppercase alphabet and endwith special character'): ")
                if accountant_id[:1:].isalpha() and accountant_id[:1:].isupper():
                    if accountant_id[-1].isalpha()==False:
                        if accountant_id[-1].isnumeric()==False:
                            cust_data.update([('govt id',accountant_id)])
                            break
                        else:
                            raise BaseException
                    else:
                        raise BaseException
                else:
                    raise BaseException
            except:
                print('Enter valid Govtment ID')
        while True:
            try:
                enter_amount=input('Amount to be deposited to the account: ')
                if enter_amount.isnumeric() and len(enter_amount)>0:
                    cust_data.update([('amount',int(enter_amount))])
                    break
                else:
                    raise BaseException
            except:
                print('Enter valid amount')
        account_number=random.randrange(10000,99999)
        if account_number not in all_cust_data:
            all_cust_data.update([(account_number,cust_data)])
            print(f'Your details are added successfully')
            print(f'Your account number is {account_number}')
            print("Please don't lose it")
            print(all_cust_data)
            break

def validation():
    while True:
        try:
            operation_to_perform=input('Account Balance Enter-1,Withdrawal Enter-2,To Deposit Enter-3: ')
            if operation_to_perform in ('1','2','3'):
                return operation_to_perform

            else:
                raise BaseException
        except:
            print('Enter valid Operation to perform')
            
def existing_user():
    global all_cust_data,account_detail
    while True:
        existing_user_acc_number=int(input('Enter account number: '))
        if existing_user_acc_number in all_cust_data:
            accountant_operation=validation()
            if accountant_operation=='1':
                account_details=all_cust_data[existing_user_acc_number]
                balance_amount=account_details.get('amount')
                print(f'Available Balance is {balance_amount}')
                break
            elif accountant_operation=='2':
                while True:
                    amount_to_withdrawal=int(input('Enter Amount to Withdrawal: '))
                    account_details=all_cust_data[existing_user_acc_number]
                    balance_amount=account_details.get('amount')
                    if balance_amount>amount_to_withdrawal:
                        balance_in_account=balance_amount-amount_to_withdrawal
                        print(F'Withdrawal amount is {amount_to_withdrawal}')
                        print(f'Balance Amount in your Account is {balance_in_account}')
                        account_details.update([('amount',balance_in_account)])
                        break
                    elif balance_amount<amount_to_withdrawal:
                        print('Insufficient Amount')
                        second_chance=input('TO enter valid amount Enter-1: ')
                        if second_chance!='1':
                            break
            elif accountant_operation=='3':
                amount_to_deposite=int(input('Enter Amount to Withdrawal: '))
                account_details=all_cust_data[existing_user_acc_number]
                balance_amount=account_details.get('amount')
                balance_in_amount1=balance_amount+amount_to_deposite
                print(f'Deposited amount is {amount_to_deposite}')
                print(f'Balance Amount in your Account is {balance_in_account1}')
                account_details.update([('amount',balance_in_account1)])
                break
        else:
            print('Account Not excist')
            print('Exit')
            break
def bank_operations():
    print("WELCOME TO 'ABC'BANK")
    while True:
        user_input=input("To Open New Account Enter-1, Existing Account user Enter-2: ")
        if user_input=='1':
            bank_account()
            user_action=input('TO EXIT enter yes: ')
            if user_action in ('YES','yes','Yes'):
                print('Thank you for Banking withus.')
                break
        elif user_input=='2':
            if len(all_cust_data)!=0:
                existing_user()
                user_action2=input('TO EXIT enter yes: ')
                if user_action2 in ('YES','yes','Yes'):
                    print('Thank you for Banking withus.')
                    break
            else:
                print('First need to create Account')
                
bank_operations()
