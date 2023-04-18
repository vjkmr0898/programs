from tkinter import *
from tkinter import messagebox,ttk
import mysql.connector
import datetime as dt

root=Tk()

class Crud:
    db=mysql.connector.connect(host='localhost',user='root', password='123134', database='inventory')
    mycur=db.cursor()
    def login_validation(self):
        login=login_mail_id.get()
        pw=login_pswd.get()

        self.mycur.execute(''' select * from admin_details''')
        for i in self.mycur.fetchall():
            try:
                if login==i[1] and  pw==i[2]:
                    self.create_widgets()
                else:
                    raise Exception
            except:
                messagebox.showerror("Error","Invalid email and Password.")
    def create_widgets(self):
        root3=Tk()
        root3.title("CRUD operation")
        root3.configure(background='yellow')
        root3.geometry('500x500')
        Label(root3,text="Inventory management",font='bold',fg='white',bg='lightgreen',width=300).pack()

        #Create buttons for CRUD operations
        
        read_btn = Button(root3, text="Read",width=15,bg='blue',fg='white',command=self.read).place(x=180,y=130)

        update_btn = Button(root3, text="Update",width=15,bg='blue',fg='white',command=self.update).place(x=180,y=180)

        delete_btn = Button(root3, text="Delete",width=15,bg='blue',fg='white',command=self.delete).place(x=180,y=230)

    def read(self):
        root4=Tk()
        root4.geometry('500x500')
        root4.configure(background='yellow')
        Label(root,text="Items in store",font='bold',fg='white',bg='lightgreen',width=300).pack()
        self.mycur.execute('select * from book_inventory')
        items_are=self.mycur.fetchall()
        for i in range(len(items_are)):
            for j in range(len(items_are[0])):
                books= Entry(root4, width=14, fg='blue',font=('Arial',10,'bold'))
                books.grid(row=i, column=j)
                books.insert(END, items_are[i][j])
    def update_value(self):
        id_=user_entered_id.get()
        column_=column.get()
        print(column_)
        value_=value.get()
        print(value_)
        if column_.lower()=='quantity' or column_.lower()=='price':
            value_ch=int(value_)
            self.mycur.execute(f'''update book_inventory set {column_}={value_ch} where id={id_}''')
            self.db.commit()
        else:
            value_ch=value_
            self.mycur.execute(f'''update book_inventory set {column_}='{value_ch}' where id={id_}''')
            self.db.commit()
        self.create_widgets()

    def update(self):
        global column,value,user_entered_id
        root5=Tk()
        root5.geometry('500x500')
        root5.configure(background='yellow')
        Label(root,text="Update Inventory",font='bold',fg='white',bg='lightgreen',width=300).pack()
        user_entered_id=IntVar(root5)
        column=StringVar(root5)
        value=StringVar(root5)

        Label(root5, text="Enter Items ID",width=20,font=("bold", 10)).place(x=80,y=130)
        Entry(root5,textvariable=user_entered_id).place(x=240,y=130)
        Label(root5, text="Enter column name",width=20,font=("bold", 10)).place(x=80,y=180)
        Entry(root5,textvariable=column).place(x=240,y=180)
        Label(root5, text="Change Value",width=20,font=("bold", 10)).place(x=80,y=230)
        Entry(root5,textvariable=value).place(x=240,y=230)
        Button(root5,text="Submit",width=10,bg='brown',fg='white',command=self.update_value).place(x=180,y=280)
    def delete_row(self):
        id_del=user_entered_id.get()
        self.mycur.execute(f'''delete from book_inventory where id={id_del}''')
        self.db.commit()
        self.create_widgets()
    def delete(self):
        global user_entered_id
        root6=Tk()
        root6.geometry('500x500')
        root6.configure(background='yellow')
        Label(root,text="Delete Items in Inventory",font='bold',fg='white',bg='lightgreen',width=300).pack()
        user_entered_id=IntVar(root6)
        Label(root6, text="Enter item ID",width=20,font=("bold", 10)).place(x=80,y=130)
        Entry(root6,textvariable=user_name).place(x=240,y=130)
        Button(root6,text="Submit",width=10,bg='brown',fg='white',command=self.delete_row).place(x=180,y=280)

class Book_store(Crud):
    def customer_details(self):
        name_=user_name.get()
        email_=user_mail_id.get()
        ph_number_=user_ph_number.get()
        try:
            self.mycur.execute(f"insert into cust_details(cust_name,cust_email,cust_ph_number) values ('{name_}','{email_}','{ph_number_}')")
            self.db.commit()
        except BaseException as msg:
            print(msg)
    def cart(self):
        date=dt.datetime.now()
        today=f'{date:%B %d, %Y}'
        root8=Tk()
        root8.geometry('500x500')
        root8.configure(background='pink')
        ids=selected_id.get()
        quantity=items_quantity.get()
        self.mycur.execute(f'select id,book_title,author,price from book_inventory where id={ids}')
        items_are=self.mycur.fetchall()
        print(items_are)
        for i in items_are:
            self.mycur.execute(f''' insert into sales(cust_name,book_id,title,author,price,quantity,date) values('{user_name.get()}',{i[0]},'{i[1]}','{i[2]}',{i[3]*quantity},{quantity},'{today}')''')
            self.db.commit()
        self.mycur.execute(f'select book_inventory.quantity-{quantity}  from book_inventory inner join sales on sales.book_id=book_inventory.id  where book_inventory.id={ids}')
        qty_price=self.mycur.fetchone()
        print(qty_price)
        self.mycur.execute(f'update book_inventory set quantity={qty_price[0]} where id={ids}')
        self.db.commit()
        self.mycur.execute(f'select cust_name,title,author,price,quantity,date from sales')
        bill=self.mycur.fetchall()
        head=[('CUSTOMER NAME','TITLE','AUTHOR','PRICE','QUANTITY','DATE')]
        for i in range(len(head)):
            for j in range(len(head[0])):
                book= Entry(root8, width=12, fg='black',font=('Arial',10,'bold'))
                book.grid(row=i, column=j)
                book.insert(END, head[i][j])
        for k in range(len(bill)):
            for l in range(len(bill[0])):
                book1= Entry(root8, width=12, fg='black',font=('Arial',10,'bold'))
                book1.grid(row=k+1, column=l)
                book1.insert(END, bill[k][l])
        Button(root8,text="OK",width=10,bg='brown',fg='white',command=self.cart).place(x=180,y=200)
    def items(self):
        global date,selected_id,items_quantity
        root1=Tk()
        root1.geometry('500x500')
        root1.configure(background='pink')
        self.mycur.execute('select id,book_title,author,price from book_inventory')
        items_are=self.mycur.fetchall()
        head=[('ITEM ID','TITLE','AUTHOR','PRICE')]
        for i in range(len(head)):
            for j in range(len(head[0])):
                book= Entry(root1, width=19, fg='black',font=('Arial',10,'bold'))
                book.grid(row=i, column=j)
                book.insert(END, head[i][j])                
        for k in range(len(items_are)):
            for l in range(len(items_are[0])):
                books= Entry(root1, width=19, fg='blue',font=('Arial',10,'bold'))
                books.grid(row=k+1, column=l)
                books.insert(END, items_are[k][l])
        Label(root1,text=" SALE ",width=40,bg="red",fg= "white").place(x=112,y=190)
        date=StringVar(root1)
        selected_id=IntVar(root1)
        items_quantity=IntVar(root1)
        Label(root1, text="Date",width=14,font=("bold", 10)).place(x=80,y=230)
        Entry(root1,textvariable=date).place(x=240,y=230)
        Label(root1, text="Item id",width=14,font=("bold", 10)).place(x=80,y=230)
        Entry(root1,textvariable=selected_id).place(x=240,y=230)
        Label(root1, text="Quantity",width=14,font=("bold", 10)).place(x=80,y=280)
        Entry(root1,textvariable=items_quantity).place(x=240,y=280)    
        Button(root1,text="OK",width=10,bg='brown',fg='white',command=self.cart).place(x=180,y=320)


    #validation for home page
    def validate(self):
        self.mycur.execute('select * from cust_details')
        all_deatils=self.mycur.fetchall()
        name=user_name.get()
        email=user_mail_id.get()
        ph_number=user_ph_number.get()
        if not name or not email or not ph_number:
            messagebox.showerror("Error","Please fill in all fields.")
        elif not "@" in email:
            messagebox.showerror("Error","Invalid email address.")
        elif ph_number.isnumeric()!=True or len(ph_number)!=10:
            messagebox.showerror("Error","Enter valid phone number.")
        else:
            for i in all_deatils:
                if email in i:
                    messagebox.showerror("Error","Email address already exsits.")
                    if ph_number in i:
                        messagebox.showerror("Error","Phone Number already exsits.")
            try:
                self.items()
                self.customer_details()
            except BaseException as msg:
                print(msg)
    def admin(self):
        global login_mail_id,login_pswd
        root2=Toplevel(root)
        root2.geometry('500x500')
        root2.configure(background='pink')
        root2.title("Inventory")
        login_mail_id=StringVar(root2)
        login_pswd=StringVar(root2)
        Label(root2,text=" LOGIN PAGE ",width=30,bg="red",fg= "white").place(x=145,y=53)   
        Label(root2, text="Mail-Id",width=15,font=("bold", 10)).place(x=80,y=130)
        Entry(root2,textvariable=login_mail_id).place(x=240,y=130)
    
        Label(root2, text="Password",width=15,font=("bold", 10)).place(x=80,y=230)

        Entry(root2,textvariable=login_pswd).place(x=240,y=230)

        Button(root2,text="LOGIN",width=10,bg='brown',fg='white',command=self.login_validation).place(x=180,y=380)

    #home page
    def home_page(self):
        global user_name,user_mail_id,user_ph_number
        root.title("Bookstore Inventory and Sales Management System")
        root.geometry('500x500')
        root.configure(background='white')
        Label(root,text="Welcome to Bookstore",font='bold',fg='white',bg='lightgreen',width=300).pack()
        
        user_name=StringVar(root)
        user_mail_id=StringVar(root)
        user_ph_number=StringVar(root)
    
        Button(root,text="ADMIN",height='1',width='12',bg='blue',fg='white',command=self.admin).place(x=400,y=35)
        
        Label(root, text="Name",width=14,font=("bold", 10)).place(x=80,y=130)
        Entry(root,textvariable=user_name).place(x=240,y=130)
    
        Label(root, text="E-mail ID",width=14,font=("bold", 10)).place(x=80,y=180)
        Entry(root,textvariable=user_mail_id).place(x=240,y=180)

        Label(root, text="Phone Number",width=14,font=("bold", 10)).place(x=80,y=230)
        Entry(root,textvariable=user_ph_number).place(x=240,y=230)

        Button(root,text="Submit",width=10,bg='brown',fg='white',command=self.validate).place(x=180,y=290)


        
o=Book_store()

o.home_page()
root.mainloop()
