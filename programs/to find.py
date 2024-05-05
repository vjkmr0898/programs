customer_name=input('enter: ')
def io():
    while True:
        try:
            if customer_name.isalpha():
                print('alpha')
                break
            else:
                raise Exception
        except:
            print('INVALID')
            break
io()
