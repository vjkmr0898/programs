import pickle
import tabulate
def createfile():
    employee_file=open('Employee.dat','wb')
    next_employee_file=open('Employee1.dat','wb')
    details=[]
    details1=[]
    while True:
        employee_id=input('Enter Employee id: ')
        employee_name=input('Enter Employee name: ')
        employee_age=input('Enter Employee age: ')
        employee_department=input('Enter Employee department: ')
        employee_salary=int(input('Enter Employee salary: '))
        in_list=[employee_id,employee_name,employee_age,employee_department,employee_salary]
        details.append(in_list)
        ch=input('To add another product Enter yes: ')
        if ch != 'yes':
            break
        elif len(details)==5:
            print('next file')
            details1.append(in_list)
    pickle.dump(details,employee_file)
    employee_file.close()
    next_employee_file.close()
def countrec(salary):
    employee_file_to_count=open('Employee.dat','rb')
    employee_count=pickle.load(employee_file_to_count)
    data=[]
    for i in employee_count:
        if i[-1]>=salary:
            data.append(i)
    print(tabulate.tabulate(data,['Emp id','Emp name','Emp age','Emp department','Emp salary']))
    employee_file_to_count.close()
def increasesalary(emp_id):
    employee_file=open('Employee.dat','rb+')
    emp_details=pickle.load(employee_file)
    final=0
    for i in emp_details:
        if i[0]==emp_id:
            i[-1]=i[-1]+2000
            final=1
            break
    if final==1:
        employee_file.seek(0)
        pickle.dump(emp_details,employee_file)
    employee_file.close()
def read_details():
    employee_file=open('Employee.dat','rb')
    emp_detail=pickle.load(employee_file)
    data=[]
    for i in emp_detail:
        data.append(i)
    print(tabulate.tabulate(data,['Emp id','Emp name','Emp age','Emp department','Emp salary']))
    employee_file.close()
print('Insert details of Employees')
createfile()
while True:
    user_ch=int(input('To get the count of emp enter-1,To increases salary Enter-2,TO read a file Enter-3,To Exit Enter-0:'))
    if user_ch==2:
        emps_id=input('Enter employee id to increase the salary Rs.2000/-: ')
        increasesalary(emps_id)
    elif user_ch==1:
        emps_salary=int(input('Enter the salary amount to get employees getting above and equal: '))
        countrec(emps_salary)
    elif user_ch==3:
        read_details()
    elif user_ch==0:
        break




















    
