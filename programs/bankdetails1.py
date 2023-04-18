import bankmodule1
def user_detail_1():
    global name,phone_number
    name_of_applicant=input('Enter your name: ')
    phone_number=input('Enter your number: ')
    address=input('Enter your address: ')
    pincode=input('Enter your pincode: ')
def user_detail_2():
    aadhar_number=input('Enter Aadhar number: ')
    verified_number=bankmodule1.check_aadhar(aadhar_number)
    if verified_number=='Enter valid Aadhar':
        user_detail_2()
    else:
        return verified_number
def bank_details():
    user_detail=user_detail_1()
    applicant_name=bankmodule1.name(name_of_applicant)
    if user_detail!=name_of_applicant=:
        print(applicant_name)
        user_detail_1()
    elif user_detail!=:
        print('Enter valid phone number')
        user_detail_1()
    elif user_detail=='Enter valid adress':
        print('Enter valid adress')
        user_detail_1()
    elif user_detail=='Enter valid pincode':
        print('Enter valid pincode')
        user_detail_1()
    else:
        user_aadhar_detail=user_detail_2()
        computer_generated_otp=bankmodule1.computer_otp()
        print(f'Your Aadhar number {user_aadhar_detail} is successfully linked with your mobile number')
        print(f'{computer_generated_otp} number as been sent to your register mobile number {phone_number[:2]}{phone_number[-2:-1]}')
        user_otp=input('Enter the OTP: ')
        if computer_generated_otp==int(user_otp):
            account_num=bankmodule1.account_number()
            mobile_number=bankmodule1.user_ph_number(phone_number)
            print('Choose which Account you are trying to open in our Bank')
            print('1. Savings Account')
            print('2. Current Account')
            user_choice=int(input('Enter your Choice:'))
            alter_name=bankmodule1.alter_name(name)
            last_name=bankmodule1.last_name(name)
            if user_choice==1:
                print('Thank you Choosing Savings Account, you should have 500 as minimum Balance.')
                print(f'And your Account Number is {alter_name[:3]}SAV{account_num}{mobile_number}.')
            elif user_choice==2:
                print('Thank you Choosing Current Account, you should have 5000 as minimum Balance.')
                print(f'And your Account Number is {last_name[:3]}CUR{account_num}{mobile_number}.')
bank_details()
