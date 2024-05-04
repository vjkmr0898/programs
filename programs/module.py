import module1  #importing module
def user_input():
    enter_name=input('Enter names seperate by comma: ')
    name_to_add=input('Enter name to add: ')
    final_list=module1.converting_input(enter_name,name_to_add) #calling converting_input function from module1 
    print(final_list)
    print(dir(module1))
    count_of_name=input('Enter the name to get a count: ')
    countOf_name=module1.count_of_element(final_list,count_of_name)  #calling count_of_element function from module1
    print(f'The count of {count_of_name} is {countOf_name}')
user_input()
