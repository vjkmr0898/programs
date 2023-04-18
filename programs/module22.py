#uploadded date 3/1/23
import random
def userlogin(user_mail_id):
    if 10<=len(user_mail_id)<=35:
        if user_mail_id[0]!='@' and user_mail_id[-1]!='@':
            if  0<user_mail_id.count('@')<2:
                if user_mail_id.isspace()==False:
                    if len(user_mail_id):
                        return user_mail_id
                else:
                    return 'Enter valid mail id'
            else:
                return 'Enter valid mail id'
        else:
            return 'Enter valid mail id'
    else:
        return 'Enter valid mail id'
def pass_word(user_password):
    if 3<=len(user_password)<=9:
        if user_password[0]!=' ' and user_password[-1]!=' ':
            if user_password[0]!='#' and user_password[-1]!='&':
                if user_password[0].isalnum()!=True: 
                    return user_password
                else:
                    return'Enter valid password'
            else:
                return'Enter valid password'
        else:
            return 'Enter valid password'
    else:
        return 'Enter valid password'
def computer_otp():
    return random.randrange(1000,10000)
def name_check(name):
    entered_name=name.split()
    if len(entered_name)>1:
        length=0
        for i in entered_name:
            if i.isalpha():
                length=length+1
        if len(entered_name)==length:
            return name
        else:
            return 'Enter valid name'
    else:
        if entered_name[0].isalpha():
            return name
        else:
            return 'Enter valid name'
def number_check(number):
    if number.isnumeric() and len(number)==10:
        return number
    else:
        return 'Enter valid number'
def otp_check(otp):
    if otp.isnumeric() and len(otp)==4:
        return otp
    else:
        return 'Enter valid otp'
