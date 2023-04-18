import module22
users_mail_id_and_password={}
def user_inputs():
    global register_for_login
    register_for_login=input('Enter mail id: ')
    password=input('Enter paasword: ')
    mail_name=module22.userlogin(register_for_login)
    id_password=module22.pass_word(password)
    if mail_name=='Enter valid mail id':
        return mail_name
    elif id_password=='Enter valid password':
        return id_password
    else:
        users_mail_id_and_password.update({mail_name:id_password})
        return mail_name

def validate():
    global computer_otp
    user_name=input('Enter name:')
    user_phone_number=input('Enter phone number: ')
    user_otp=input('Enter 4-digit OTP: ')
    computer_otp=module22.computer_otp()
    entered_name=module22.name_check(user_name)
    entered_number=module22.number_check(user_phone_number)
    entered_otp=module22.otp_check(user_otp)
    if entered_name==user_name and entered_number==user_phone_number and entered_otp==user_otp: 
        return user_otp
    else:
        print('Enter valid character')
        validate()
def user_input():
    count=0
    while count<5:
        mailid_and_password=user_inputs()
        count=count+1
        if register_for_login==mailid_and_password:
            name_number_otp=validate()
            if computer_otp==name_number_otp:
                print('------------------------Welcome-------------------------')
                print('You are now registered to our Application, now you can use our application any time using your mail id and password.')
        else:
            user_inputs()
    
user_input()
