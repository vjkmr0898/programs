#uploaded in 3/1/23
import random
def name_applicant(user_name):
    if user_name.isalpha():
        return user_name
    else:
        return 'Enter valid name'
def user_mobile_number(mobile_number):
    consecutive_count=0
    if mobile_number.isnumeric() and len(mobile_number)==10:
        if mobile_number[0]=='9':
            alter1=mobile_number[::2]
            alter2=mobile_number[1::2]
            for i in zip(alter1,alter2):
                if i[0]==0 and i[1]==0:
                    consecutive_count=consecutive_count+1
            if consecutive_count>0:
                return 'No consecutive number'
        else:
            return 'Enter valid phone number'
    else:
        return 'Enter valid phone number'
def addres(user_address):
    if user_address.isalpha():
        return user_address
    else:
        return 'Enter valid adress'
def pincode(user_pincode):
    if user_pincode.isnumeric():
        return user_pincode
    else:
        return 'Enter valid pincode'
def check_aadhar(user_aadhar_number):
    if len(user_aadhar_number)==12:
        converting=user_aadhar_number.partition(user_aadhar_number[4:8])
        converted_in_list=[]
        for i in converting:
           converted_in_list.append(i)
        return '-'.join(converted_in_list)
    else:
        return 'Enter valid Aadhar'
def computer_otp():
    return random.randrange(100000,1000000)
def account_number():
    return random.randrange(1000,10000)
def user_ph_number(number):
    mob_num=''
    count=0
    for i in range(0,len(number),2):
        if count<4:
            mob_num=mob_num+number[i]
            count=count+1
    return mob_num
def alter_name(accountant_name):
    changed_name=''
    count1=0
    for i in range(0,len(accountant_name)+1,2):
        if count1<3:
            if accountant_name[i] not in 'AEIOUaeiou':
                changed_name=changed_name+accountant_name[i]
                count1=count1+1
    return changed_name
def last_name(user_last_name):
    count2=0
    last_name1=''
    for i in range(len(user_last_name)-1,0,-2):
        if count2<3:
            if user_last_name[i] not in 'aeiouAEIOU':
                last_name1=last_name1+user_last_name[i]
                count2=count2+1
    return last_name1
