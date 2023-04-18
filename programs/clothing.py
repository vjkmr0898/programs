import mysql.connector
import random
import tabulate
class Db_connection:
    def __init__(self):
        self.connection=mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='123134',
                                           database='inventory')
db_connect=Db_connection()
class Cart:
    def __init__(self):
        self.cust_name=input('Enter your name: ')
        print('Welcome to the Clothing Store Inventory Management System!')
    def available_items(self):
        cursor=db_connect.connection.cursor()
        in_list=[]
        cursor.execute(f'''select * from clothing_inventory''')
        for i in cursor.fetchall():
            in_list.append([i[0],i[1],i[2],i[3],i[4]])
        print(tabulate.tabulate(in_list,['ITEM ID','CATEGORY','BRAND','SIZE','PRICE']))
    def table_creation(self):
        cursor=db_connect.connection.cursor()
        cursor.execute('''create table if not exists customer_cart(cust_id int not null,items_id int not null,
                        categories varchar(255) not null,brand varchar(255) not null,size varchar(5) not null,
                        no_of_items decimal(10,2) not null,price decimal(10,2),
                        foreign key(items_id) references clothing_inventory(items_id))''')
    def browse_clothing_items(self):
        cursor=db_connect.connection.cursor()
        ch=int(input('''Display available clothing items by
                    category Enter-1,
                    Brand Enter-2,
                    Price range Enter-3,
                    Size Enter-4
                    Enter: '''))
        if ch==1:
            category_name=input('Enter the category: ')
            print(category_name)
            cursor.execute(f'''select * from clothing_inventory where categories='{category_name.title()}' ''')
            for i in cursor.fetchall():
                print(f'Category: {i[1]}')
                print(f'Brand: {i[2]}')
                print(f'Size: {i[3]}')
                print(f'Price: {i[4]}')
                print()
        elif ch==2:
            brand=input('Enter the Brand: ')
            cursor.execute(f"select * from clothing_inventory where brand='{brand.title()}' ")
            for i in cursor.fetchall():
                print(f'Category: {i[1]}')
                print(f'Brand: {i[2]}')
                print(f'Size: {i[3]}')
                print(f'Price: {i[4]}')
                print()
        elif ch==3:
            starting_price=float(input('Enter the price range: '))
            ending_price=float(input('Enter the Ending price: '))
            cursor.execute(f'''select * from clothing_inventory where  price between {starting_price} and {ending_price}''')
            for i in cursor.fetchall():
                print(f'Category: {i[1]}')
                print(f'Brand: {i[2]}')
                print(f'Size: {i[3]}')
                print(f'Price: {i[4]}')
                print()
        elif ch==4:
            size=input('Enter the Size: ')
            cursor.execute(f'''select * from clothing_inventory where categories='{size.upper()}' ''')
            for i in cursor.fetchall():
                print(f'Category: {i[1]}')
                print(f'Brand: {i[2]}')
                print(f'Size: {i[3]}')
                print(f'Price: {i[4]}')
                print()
    def add_item_to_cart(self):
        cust_id=self.cust_name[:2].upper()+str(random.randrange(10,21))
        while True:
            cursor=db_connect.connection.cursor()
            items_id=int(input("Enter item's id to add item to cart: "))
            no_of_items=int(input("Enter Number of items add to cart: "))
            cursor.execute(f'''select * from clothing_inventory where items_id={items_id}''')
            item=cursor.fetchone()
            cursor.execute(f'''insert into customer_cart values ('{cust_id}',{item[0]},'{item[1]}','{item[2]}','{item[3]}',{no_of_items},{no_of_items*item[4]})''')
            db_connect.connection.commit()
            ch=input("To add another product to cart Enter yes: ")
            if ch!='yes':
                break
    def view_cart(self):
        cursor=db_connect.connection.cursor()
        cursor.execute('''select * from  customer_cart''')
        for i in cursor.fetchall():
            print(f"Item's id: {i[0]}")
            print(f'Category: {i[1]}')
            print(f'Brand: {i[2]}')
            print(f'Size: {i[3]}')
            print(f'Price: {i[4]}')
            print()
    def checkout(self):
        cursor=db_connect.connection.cursor()
        cursor.execute('''select * from  customer_cart''')
        in_list=[]
        for i in cursor.fetchall():
            in_list.append([i[0],i[1],i[2],i[3],i[4],i[4],i[5]])
        cursor.execute('''select sum(price) from  customer_cart''')
        total_price=cursor.fetchone()
        print(tabulate.tabulate([in_list],['CUSTOMER ID','ITEM ID','CATEGORY','BRAND','SIZE','NO.OF ITEMS','PRICE']))
        print(f'Amount to pay: {total_price[0]}')
class Inventory:
    def add_clothing_item(self):
        cursor=db_connect.connection.cursor()
        while True:
            category=input('Enter Category name: ')
            brand=input('Enter Brand name: ')
            size=input('Enter Size: ')
            price=int(input('Enter the item price: '))
            cursor.execute(f'''insert into clothing_inventory (categories,brand,size,price)
            values ('{category.title()}','{brand.title()}','{size.upper()}',{price})''')
            db_connect.connection.commit()
            ch=input("To add another product to inventory Enter yes: ")
            if ch!='yes':
                break
    def retrieve_clothing_item(self):
        cursor=db_connect.connection.cursor()
        item_id=int(input('Enter Items id: '))
        cursor.execute(f'''select * from clothing_inventory where items_id={item_id}''')
        for i in cursor.fetchall():
            print(f'Category: {i[1]}')
            print(f'Brand: {i[2]}')
            print(f'Size: {i[3]}')
            print(f'Price: {i[4]}')
            print()
    def update_clothing_item(self):
        cursor=db_connect.connection.cursor()
        while True:
            item_id=int(input('Enter Items id: '))
            cursor.execute(f'''select * from clothing_inventory where items_id={item_id}''')
            for i in cursor.fetchall():
                print(f'Category: {i[1]}')
                print(f'Brand: {i[2]}')
                print(f'Size: {i[3]}')
                print(f'Price: {i[4]}')
                print()
            column_name=input('Enter column name to change: ')
            if column_name!='price':
                changed_value=input('Enter the new value: ').title()
            elif column_name=='price':
                changed_value=int(input('Enter the new value: '))
            cursor.execute(f'''update clothing_inventory set {column_name}='{changed_value}' where items_id={item_id}''')
            db_connect.connection.commit()
            ch=input("To add another product to inventory Enter yes: ")
            if ch!='yes':
                break
    def remove_clothing_item(self):
        cursor=db_connect.connection.cursor()
        while True:
            item_id=int(input('Enter the item ID: '))
            cursor.execute(f''' delete from clothing_inventory where {item_id}''')
            db_connect.connection.commit()
            ch=input("To delete another item from inventory Enter yes: ")
            if ch!='yes':
                break
    def view_orders(self):
        cursor=db_connect.connection.cursor()
        cursor.execute(f'''select * from clothing_inventory inner join customer_cart on customer_cart.items_id=clothing_inventory.items_id''')
        for i in cursor.fetchall():
            print(f'Item Id: {i[0]}')
            print(f'Category: {i[1]}')
            print(f'Brand: {i[2]}')
            print(f'Size: {i[3]}')
            print(f'Price: {i[4]}')
            print(f'Customer id: {i[5]}')
            print(f"Selected item's category: {i[7]}")
            print(f"Selected item's brand: {i[8]}")
            print(f"Selected item's size: {i[9]}")
            print(f"Selected item's No.of items: {i[10]}")
            print(f"Selected item's price: {i[11]}")
            print()

user=int(input('''
Customer Enter-0
Shopkeeper Enter-1
Enter: '''))
if user==0:
    print('''
    Enter-1 for Browse clothing items
    Enter-2 for Add item to cart
    Enter-3 for View cart
    Enter-4 for Checkout
    Enter-5 for Exit
    ''')
    customer=Cart()
    while True:
        customer.available_items()
        user_ch=int(input('Enter your choice: '))
        if user_ch==1:
            customer.browse_clothing_items()
        elif user_ch==2:
            customer.add_item_to_cart()
        elif user_ch==3:
            customer.view_cart()
        elif user_ch==4:
            customer.checkout()
        elif user_ch==5:
            break
elif user==1:
    print('''
    Enter-1 for Add clothing item
    Enter-2 for Retrieve clothing item
    Enter-3 for Update clothing item
    Enter-4 for Remove clothing item
    Enter-5 for View orders
    Enter-6 for Exit''')
    seller=Inventory()
    while True:
        shopkeeper_ch=int(input('Enter your choice: '))
        if shopkeeper_ch==1:
            seller.add_clothing_item()
        elif shopkeeper_ch==2:
            seller.retrieve_clothing_item()
        elif shopkeeper_ch==3:
            seller.update_clothing_item()
        elif shopkeeper_ch==4:
            seller.remove_clothing_item()
        elif shopkeeper_ch==5:
            seller.view_orders()
        elif shopkeeper_ch==6:
            break





