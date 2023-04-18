import tabulate
import random
customer_id=input('Enter customer id: ')
class Customer_details:
    customer_details={}    #to store customer details with customer id as keya and name,number as value
    super_market='VMART'  #super market name 
    customers_items={}   #customer choosen itmes
    product_in_vmart={101:['Salt(1kg)',55.00],102:['Bread',25.00],103:['Oil(1l)',115.00],104:['Coffe powder',55.00],105:['Soap',45.00],106:['Chips',35.00],107:['Biscuits',30.00],108:['Peanuts',5.00],109:['Yogurt',50.00],110:['Milf(1l)',55.00]}
    def __init__(self,customers_id):
        self.customers_id=customers_id
#method for new user need to sign up and get details
    def sign_up(self):
        while True:
            try:
                user_name=input('Enter name: ')
                if user_name.isalpha() and len(user_name)>0:
                    name=user_name
                    break
                else:
                    raise BaseException
            except:
                print('Enter valid name')
        while True:
            try:
                user_mobile_number=input('Enter Mobile Number: ')
                if user_mobile_number.isnumeric() and len(user_mobile_number)>0:
                    number=user_mobile_number
                    break
                else:
                    raise BaseException
            except:
                print('Enter valid number')
        while True:
            try:
                user_location=input('Enter location: ')
                if user_location.isalpha() and len(user_location)>0:
                    location=user_location
                    break
            except:
                print('Enter valid location')
        generated_number=random.randrange(1000,10000)
        self.customers_id=f'{Customer_details.super_market[:2:]}{generated_number}{location[:2:].upper()}'
        print(f'Registration is done and your id is {self.customers_id}')
        Customer_details.customer_details.update([(self.customers_id,[name,number])])
    #method to show the items in super market
    def productsin_vmart(self):
        print('Items available in stores')
        product_in_vmart_data=[]
        item_code=101
        for i,j in Customer_details.product_in_vmart.items():
            product_in_vmart_data.append([i,j[0],1,j[1]])
            item_code=item_code+1
        print(tabulate.tabulate(product_in_vmart_data,['ITEMS CODE','ITEMS','QUANTITY','PRICE']))
    #method for customer to select the product and quantity
    def customer_cart(self):
        while True:
            user_choosen_product=int(input('Enter the Items code to purchase: '))
            product_quantity=int(input('Enter the Items quantity: '))
            if user_choosen_product in Customer_details.product_in_vmart:            
                Customer_details.customers_items.update([(user_choosen_product,product_quantity)])
            elif user_choosen_product not in Customer_details.product_in_vmart:
                print('Item not available,May be in Available in Discount Sale')
            user_choice=input("To continue shopping enter 'yes': ")
            if user_choice.title()=='Yes':
                pass
            elif user_choice.title()=='No':
                break
            else:
                print('Enter valid input')
class Customer_bill(Customer_details):
    delivery_charge=0
    for_bill=[]
    s_no=1
    discount_items={201:['Sugar(1kg)',[60.00,'5%']],202:['Sugar(5kg)',[60.00,'10%']],203:['Rice(10kg)',[75.00,'4%']],204:['Rice(25kg)',[75.00,'8%']],205:['Atta(5kg)',[38.00,'6%']],206:['Atta(10kg)',[38.00,'12%']]}
    dicount_percentage={201:5,202:10,203:4,204:8,205:6,206:12}
    def __init__(self,customers_id):
        Customer_details.__init__(self,customers_id)
    #method for discont product in supermarket
    def discount_products(self):
        discount_items_data=[]
        print('Discount Items')
        for i,j in Customer_bill.discount_items.items():
            discount_items_data.append([i,j[0],j[1][0],j[1][1]])
        print(tabulate.tabulate(discount_items_data,['ITEM CODE','ITEM','PRICE','DISCOUNT']))
        while True:
            user_choosen_discount_product=int(input('Enter the Item Code: '))
            discount_product_quantity=int(input('Enter quantity: '))
            if  user_choosen_discount_product in Customer_bill.discount_items:            
                Customer_details.customers_items.update([(user_choosen_discount_product,discount_product_quantity)])
            elif user_choosen_discount_product not in Customer_bill.discount_items:
                print('Item not available')
            user_choice_in_discount=input("To continue shopping enter 'yes': ")
            if user_choice_in_discount.title() == 'Yes':
                pass
            elif user_choice_in_discount.title() == 'No':
                break
            else:
                print('Enter valid input')
    # method to show available delivery location and then charge for location
    def delivery_charges(self):
        print('Delivery Location are Adayar,Besant Nagar,Indira Nagar,T-nagr')
        available_location={'Adayar':'Ad','Besant Nagar':'Bn','Indira Nagar':'In','T-nagar':'Tn'}
        loc_no=1
        charge_delivery_locations={1:20,2:40,3:50,4:70}
        for i,j in available_location.items():
            print(f'For {i} Enter-{loc_no}')
            loc_no=loc_no+1
        user_delivery_location=int(input('Enter Delivery Location number (OR) Pick up from the store Enter-0: '))
        if user_delivery_location in charge_delivery_locations.keys():
            for l in charge_delivery_locations:
                if l==user_delivery_location:
                    Customer_bill.delivery_charge=charge_delivery_locations[user_delivery_location]
                    break
        elif user_delivery_location not in available_location:
            print('Sorry delivery is not available for this location')
        elif user_delivery_location==0:
            pass
    #to calculate the total price to pay            
    def total_calculaton(self):
        for i,j in Customer_details.customers_items.items():
            if i in Customer_details.product_in_vmart:
                price_for_customer_item=Customer_details.product_in_vmart[i][1]*j
                Customer_bill.for_bill.append([Customer_bill.s_no,Customer_details.product_in_vmart[i][0],j,Customer_details.product_in_vmart[i][1],'0%',price_for_customer_item])
                Customer_bill.s_no=Customer_bill.s_no+1
            elif i in Customer_bill.discount_items.items():
                discount_items_calulation=Customer_bill.discount_items[i]
                items_dicount=Customer_bill.dicount_percentage[i]
                items_price=Customer_bill.discount_items_calulation[1][0]
                price_for_customer_discount_items=((items_dicount/100)-customer_bill.items_price)*j
                Customer_bill.for_bill.append([Customer_bill.s_no,discount_items_calulation[0],j,discount_items_calulation[1][0],discount_items_calulation[1][1],price_for_customer_discount_items])
                Customer_bill.s_no=Customer_bill.s_no+1
        total_price_to_pay=0
        for i in Customer_bill.for_bill:
            total_price_to_pay=total_price_to_pay+i[-1]
        full_details=Customer_details.customer_details[self.customers_id]
        print(f'Customer ID-{self.customers_id}')
        print(f'Name-{full_details[0]}')
        print(f'Mobile Number-{full_details[1]}')
        print(tabulate.tabulate(Customer_bill.for_bill,['S.NO','ITEM','QUANTITY','ITEM PRICE','DISCOUNT','PRICE']))
        print(f'Delivery charge is {Customer_bill.delivery_charge}')
        print(f'Total price is {total_price_to_pay+Customer_bill.delivery_charge}')
        print('Thank you')
if customer_id not in Customer_details.customer_details:
    print('Need to sign up')
    customer1=Customer_bill(customer_id)
    customer1.sign_up()
    customer1.productsin_vmart()
    customer1.customer_cart()
    customer1.discount_products()
    customer1.delivery_charges()
    customer1.total_calculaton()
else:
    customer1=Customer_bill(customer_id)
    customer1.productsin_vmart()
    customer1.customer_cart()
    customer1.discount_products()
    customer1.delivery_charges()
    customer1.total_calculation()
