import pickle
def add_products():
    add_product_to_file=open('products.bin','wb')
    in_list=[]
    while True:
        product_id=input('ENter product id: ')
        product_name=input('Enter product name: ')
        product_price=input('Enter product price: ')
        in_dictionary={product_id:[product_name,product_price]}
        in_list.append(in_dictionary)
        ch=input('To add another product Enter yes: ')
        if ch != 'yes':
            break
    pickle.dump(in_list,add_product_to_file)
    add_product_to_file.close()
def products_are():
    products_file=open('products.bin','rb')
    products=pickle.load(products_file)
    products_file.close()
    for i in products:
        for j in i:
            print(f'Product id {j},product name {i[j][0]}and its price {i[j][1]}')
def delete_product():
    product_file=open('products.bin','rb+')
    product_to_delete=input('Enter product id to remove: ')
    products=pickle.load(product_file)
    lst=[]
    for i in products:
        for j,k in i.items():
            if product_to_delete!=j:
                lst.append(i)
            else:
                print('product removed')
    pickle.dump(lst,product_file)
    product_file.close()
while True:
    print('To add product to file Enter-1')
    print('To read product enter-2')
    print('To delect product enter-3')
    print('To quit enter-0')
    user_choice=int(input('Enter your choice: '))
    if user_choice==1:
        add_products()
    elif user_choice==2:
        products_are()
    elif user_choice==3:
        delete_product()
    elif user_choice==0:
        print('Exit')
        break
