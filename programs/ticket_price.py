try:
    enter_age=int(input('Enter age: '))
    declared_price=1000
    if enter_age>0:
        if type(enter_age)==int:
            if enter_age<18:
                print(f'The discounted price based on the age is {enter_age-(enter_age*(10/100))}')
            elif 18<enter_age<30:
                print(f'The discounted price based on the age is {enter_age-(enter_age*(25/100))}')
            elif 30<enter_age<60:
                print(f'The discounted price based on the age is {enter_age-(enter_age*(30/100))}')
            elif 60<enter_age:
                print(f'The discounted price based on the age is {enter_age-(enter_age*(50/100))}')
        else:
            raise TypeError
    else:
        raise ValueError
except BaseException as be:
    print('Enter valid age')
    print(be)
finally:
    print('Thank you')
