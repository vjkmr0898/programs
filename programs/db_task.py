import mysql.connector

class My_sql:
    host='localhost'
    user_name='root'
    pw='123134'
    database_name='inventory'
    connection=mysql.connector.connect(host=host,user=user_name,password=pw,database=database_name)
    def check_connection(self):
        if My_sql.connection.is_connected():
            print('Connected')
        else:
            print('not connected')
    cursor=connection.cursor()
    def table_creation(self):
        My_sql.cursor.execute('use inventory')

        My_sql.cursor.execute(
            '''create table if not exists product(product_id int not null,product_name varchar(255) not null,
            quantity decimal(10,2) not null,unit_price decimal(10,2) not null,supplier_name varchar(255))'''
            )
    def alter_table(self):
        My_sql.cursor.execute('alter table product modify product_id int primary key auto_increment')
        My_sql.cursor.execute('desc product')
        print(My_sql.cursor.fetchall())
    def values_to_table(self):
        in_list=[]
        product_id=input('Enter product id: ')
        product_name=input('Enter product name: ')
        quantity=float(input('Enter quantity of the product: '))
        price=float(input('Enter price of the product: '))
        supplier_name=input('Enter supplier name: ')
        My_sql.cursor.execute('insert into product(product_id,product_name,quantity,unit_price,supplier_name) values (%s,%s,%s,%s,%s)',
                            (product_id,product_name,quantity,price,supplier_name))
        My_sql.connection.commit()
        My_sql.cursor.execute('select * from product')
        for i in My_sql.cursor.fetchall():
            print(i)
    def update_values(self):
        My_sql.cursor.execute("update product set supplier_name='kumar' where product_id='1'")
        My_sql.connection.commit()
        My_sql.cursor.execute('select * from product')
        for i in My_sql.cursor.fetchall():
            print(i)
    def delete(self):
        to_delete=input('Enter product_id to delete: ')
        My_sql.cursor.execute(f"delete from product where product_id={to_delete}")
        My_sql.cursor.execute("select * from product")
        print(My_sql.cursor.fetchall())
    def total_values(self):
        My_sql.cursor.execute("select (unit_price*quantity) as total from product")
        print(My_sql.cursor.fetchall())
obj=My_sql()
obj.check_connection()
obj.table_creation()
while True:
    obj.values_to_table()
    ch=input('To enter another product enter yes: ')
    if ch!='yes':
        break
obj.update_values()
obj.delete()
obj.total_values()
