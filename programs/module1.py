def converting_input(user_enter_names,add_to_list):
    list_of_names=user_enter_names.split(',')   #converting string to list
    addon_names=add_to_list.split()   #converting string to list
    return list_of_names+addon_names  #concatinate the list
def count_of_element(full_list,user_count):
    count=0                       #to get count of user_coun variable
    for i in full_list:
        if user_count == i:  
            count+=1
    return count
