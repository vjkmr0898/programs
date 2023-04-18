class My_list:
    def __init__(self, list1):
        self.list = list1
    def __add__(self,other):
        if len(self.list)==len(other.list):
            return [x + y for x, y in zip(self.list, other.list)]
        else:
            return "Can't add list of different length"
    def __sub__(self,other):
        if len(self.list)==len(other.list):
            return [x - y for x, y in zip(self.list, other.list)]
        else:
            return "Can't sub list of different length"
    def __mul__(self,other):
        if len(self.list)==len(other.list):
            return [x * y for x, y in zip(self.list, other.list)]
        else:
            return "Can't muliply list of different length"
    def __truediv__(self, other):
        if other.list.count(0)==0:
            if len(self.list)==len(other.list):
                return [x / y for x, y in zip(self.list, other.list)]
            else:
                return "Can't divide list of different length"
        else:
            return 'Division by 0 is not possible'
    def __repr__(self):
        return f'Object of the My_list class'

print('''For Addition Enter-1
For Subtraction Enter-2
For Multiplication Enter-3
For Division Enter-4''')
user_choice=int(input('Enter Your choice: '))
if user_choice==1:
    user_list1=input('Enter number seperator by comma: ')
    user_list2=input('Enter number seperator by comma: ')
    splitted_list1=user_list1.split(',')
    splitted_list2=user_list2.split(',')
    num1=list(map(int,splitted_list1))
    num2=list(map(int,splitted_list2))
    p1 = My_list(num1)
    p2 = My_list(num2)
    print(p1 + p2)
elif user_choice==2:
    user_list1=input('Enter number seperator by comma: ')
    user_list2=input('Enter number seperator by comma: ')
    splitted_list1=user_list1.split(',')
    splitted_list2=user_list2.split(',')
    num1=list(map(int,splitted_list1))
    num2=list(map(int,splitted_list2))
    p1 = My_list(num1)
    p2 = My_list(num2)
    print(p1 - p2)
elif user_choice==3:
    user_list1=input('Enter number seperator by comma: ')
    user_list2=input('Enter number seperator by comma: ')
    splitted_list1=user_list1.split(',')
    splitted_list2=user_list2.split(',')
    num1=list(map(int,splitted_list1))
    num2=list(map(int,splitted_list2))
    p1 = My_list(num1)
    p2 = My_list(num2)
    print(p1 * p2)
elif user_choice==4:
    user_list1=input('Enter number seperator by comma: ')
    user_list2=input('Enter number seperator by comma: ')
    splitted_list1=user_list1.split(',')
    splitted_list2=user_list2.split(',')
    num1=list(map(int,splitted_list1))
    num2=list(map(int,splitted_list2))
    p1 = My_list(num1)
    p2 = My_list(num2)
    print(p1 / p2)
else:
    print('Enter valid number')
