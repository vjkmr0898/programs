#uploaded at 13-1-23
import random
import tabulate
s_no=0
def cutomer_bill_number():
    enter_bill_number=input('Enter 3-digit bill number: ')
    validated_bill_number=customer_bill_number_validation(enter_bill_number)
    if enter_bill_number==validated_bill_number:
        return validated_bill_number
    else:
        print(validated_bill_number)
        cutomer_bill_number()
def customer_name():
    enter_name=input('Enter customer name: ')
    validated_name=customer_name_validation(enter_name)
    if validated_name==enter_name:
        return validated_name
    else:
        print(validated_name)
        customer_name()
def customer_name_validation(customers_name):
    if customers_name.isalpha() and len(customers_name)>0:
        return customers_name
    else:
        return 'Enter valid name'
def customer_bill_number_validation(customers_bill_number):
    if customers_bill_number.isnumeric() and len(customers_bill_number)==3:
        return customers_bill_number
    else:
        return 'Enter valid id'
def month():
    enter_no_calls_month=int(input('Enter number of month bill'))
    validatted_month=validation_of_month(enter_no_calls_month)
    if validatted_month==enter_no_calls_month:
        return validatted_month
    else:
        print(validatted_month)
def validation_of_month(customers_enter_month):
    if str(customers_enter_month).isnumeric() and len(str(customers_enter_month))>0:
        return customers_enter_month
    else:
        return 'Enter valid id'
def consumer_number():
    consumers_number=random.randint(100000,1000000)
    return consumers_number
def call_calculation(customers_no_of_calls):
    enter_no_of_calls=int(customers_no_of_calls)
    cost_for_calls=0
    if enter_no_of_calls!=0:
        if enter_no_of_calls>300:
                above_300_calls=enter_no_of_calls-300
                cost_for_calls=(100*0.06)+(100*0.08)+(100*1.20)+(above_300_calls*1.50)+125
        else:
            if enter_no_of_calls>200:
                third_100_calls=enter_no_of_calls-200
                cost_for_calls=(100*0.06)+(100*0.08)+(third_100_calls*1.20)+125
            elif enter_no_of_calls>100:
                second_100_calls=enter_no_of_calls-100
                cost_for_calls=(100*0.06)+(second_100_calls*0.08)+125
            elif enter_no_of_calls<=100:
                cost_for_calls=100*0.06+125
    else:
        cost_for_calls+=125
    return cost_for_calls
def full_details(each_bill):
    global s_no,consumer_details_in_dictionary
    consumer_details_in_dictionary={}
    consumer_details_in_dictionary.update([(s_no,each_bill)])
def table_format():
    heading=['BIIL NO','NAME','RATE','CONSUMER NUMBER','MONTHLY RATE']
    details=[]
    for i in consumer_details_in_dictionary.values():
        for j in i.keys():
            with_consumer_number=in_dictionary[j]
            details.append(with_consumer_number)
    in_table=tabulate.tabulate(details,headers=heading)
    print(in_table)
def customer_bill():
    global s_no,in_dictionary
    in_dictionary={}
    x=True
    while x==True:
        bill=cutomer_bill_number()
        name=customer_name()
        number=consumer_number()
        no_of_calls=input('Enter number of calls consumed: ')
        pay=call_calculation(no_of_calls)
        customer_month_pay=month()
        monthly_rate=pay*customer_month_pay
        in_dictionary.update([(number,[bill,name,pay,number,str(monthly_rate)])])
        s_no=s_no+1
        full_details(in_dictionary)
        customer_descition=input('Do you another person telephone bill detail Enter "yes": ')
        if customer_descition==('no' or 'NO'):
            table_format()
            x=False
            while True:
                enter_consumer_number=int(input('Enter consumer number: '))
                each_detail=in_dictionary[enter_consumer_number]
                data=[[each_detail[0],each_detail[1],each_detail[2],each_detail[4]]]
                table_for_consumer_number=tabulate.tabulate(data,['BIIL NO','NAME','RATE','MONTHLY RATE'])
                print(table_for_consumer_number)
                enter_yes_or_no=input('want another details Enter yes: ')
                if enter_yes_or_no==('no' or 'NO'):
                    print('Thank you')
                    break
customer_bill()
