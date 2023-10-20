import main_menu
import student_data
import mysql.connector as co

def STU_MENU():
    while True:
        print("\t\t..........................................................")
        print("\t\t*****Welcome To School Management System*****")
        print("\t\t..........................................................")
        print("\n\t\t*****Mao Public School*****")
        print("1: Add Student Record")
        print("2: Show Student Details")
        print("3: Search Student Record")
        print("4: Delete student records")
        print("5: Edit student record")
        print("6: Exit")
        print("\t\t----------------------------------------------------------")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            student_data.Add_Records()
        elif choice == 2:
            student_data.Show_Stu_Details()
        elif choice == 3:
            student_data.Search_Stu_Details()
        elif choice == 4:
            student_data.Delete_Stu_Details()
        elif choice == 5:
            student_data.Edit_Stu_Details()
        elif choice == 6:
            return
        else:
            print("Error: Invalid Choice. Try again.....")
        conti = "Press any key to return to Main Menu"

def Add_Records():
    try:
        mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
        cursor = mycon.cursor()
        session = input('Enter academic session (e.g., 2019-20):')
        stname = input('Enter Student Name')
        stclass = input('Enter class:')
        stsec = input('Enter section:')
        stroll = input('Enter roll no:')
        sub1 = input('Enter subject1:')
        sub2 = input('Enter subject2:')
        sub3 = input('Enter subject3:')
        query = "insert into student(session, stname, stclass, stsec, stroll, sub1, sub2, sub3) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(session, stname, stclass, stsec, stroll, sub1, sub2, sub3)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('Record has been saved in the student table')
    except:
        print('error')

def Show_Stu_Details():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    cursor.execute("select * from student")
    data = cursor.fetchall()
    for row in data:
        print(row)

def Search_Stu_Details():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Roll Number')
    st = "select * from student where stroll='%s'" % (ac)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)

def Delete_Stu_Details():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Roll Number')
    st = "delete from student where stroll='%s'" % (ac)
    cursor.execute(st)
    mycon.commit()
    print('Data deleted successfully')

def Edit_Stu_Details():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    print("1: Edit session")
    print("2: Edit name")
    print("3: Edit class")
    print("4: Edit section")
    print("5: Edit Roll no")
    print("6: Edit sub1")
    print("7: Edit sub2")
    print("8: Edit sub3")
    print("9: Return")
    print("\t\t----------------------------------------------------------")
    choice = int(input("Enter your choice"))
    if choice == 1:
        student_data.edit_session()
    elif choice == 2:
        student_data.edit_name()
    elif choice == 3:
        student_data.edit_class()
    elif choice == 4:
        student_data.edit_section()
    elif choice == 5:
        student_data.edit_Rollno()
    elif choice == 6:
        student_data.edit_sub1()
    elif choice == 7:
        student_data.edit_sub2()
    elif choice == 8:
        student_data.edit_sub3()
    elif choice == 9:
        return
    else:
        print("Error: Invalid Choice. Try again.....")
    conti = "Press any key to return to "

def edit_session():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Roll no')
    nm = input('Enter correct session')
    st = "update student set session='%s' where stroll='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

def edit_name():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Roll no')
    nm = input('Enter correct name')
    st = "update student set stname='%s' where stroll='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

def edit_class():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Roll no')
    nm = input('Enter correct class')
    st = "update student set stclass='%s' where stroll='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

def edit_section():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Roll no')
    nm = input('Enter correct section')
    st = "update student set stsec='%s' where stroll='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

def edit_Rollno():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Roll no')
    nm = input('Enter correct Roll no.')
    st = "update student set stroll='%s' where stroll='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

def edit_sub1():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Roll no')
    nm = input('Enter correct subject1')
    st = "update student set sub1='%s' where stroll='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

def edit_sub2():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Roll no')
    nm = input('Enter correct subject2')
    st = "update student set sub2='%s' where stroll='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

def edit_sub3():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Roll no')
    nm = input('Enter correct subject3')
    st = "update student set sub3='%s' where stroll='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')
