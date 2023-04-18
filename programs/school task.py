def school_records():
    import tabulate
    adding_detail=[]
    x=True
    while x==True:
        roll_number=int(input('Enter a roll number:-'))
        name=input('Enter name:-')
        total_mark=int(input('Enter Total marks:-'))
        to_quit=input('Do you want to quit enter yes =')
        details=(roll_number,name,total_mark)
        adding_detail.append(details)
        if to_quit=='yes':
            x=False
            student_details=tuple(adding_detail)
            print(student_details)
            header=['S.No.', 'RollNo', 'Name', 'Total']
            s_no=1
            data=[]
            for i in range(1,len(student_details)+1):
                data.append((student_details[i-1][0],student_details[i-1][1],student_details[i-1][2]))
            print(tabulate(data,headers=header,tablefmt='solid',showindex='always'))
            high_score=0
            for j in student_details:
                if j[-1]>high_score:
                    high_score=j[-1]
            high_score_student=high_score
            for k in student_details:
                if high_score_student==k[-1]:
                    print('Highest Aggregate scorer is')
                    print(f'{k[0]} {k[1]} {k[2]}')
school_records()
