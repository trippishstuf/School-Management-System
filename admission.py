import main_menu
import admission
import mysql.connector as co

def ADM_MENU():
    while True:
        print("\t\t..........................................................")
        print("\t\t*****Welcome To School Management System*****")
        print("\t\t..........................................................")
        print("\n\t\t*****Mao Public School*****")
        print("1: Admission Details")
        print("2: Show admission details")
        print("3: Search")
        print("4: Deletion of records")
        print("5: Update Admission Details")
        print("6: Return")
        print("\t\t----------------------------------------------------------")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            admission.admn_details()
        elif choice == 2:
            admission.show_admn_details()
        elif choice == 3:
            admission.search_admn_details()
        elif choice == 4:
            admission.delete_admn_details()
        elif choice == 5:
            admission.edit_admn_details()
        elif choice == 6:
            return
        else:
            print("Error: Invalid Choice try again.....")
        conti = "Press any key to return to Main Menu"

def admn_details():
    try:
        mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
        cursor = mycon.cursor()
        adno = input('Enter Admission number')
        rno = int(input('Enter Roll no'))
        sname = input('Enter student name')
        address = input('Enter address')
        phon = input('Enter phone number')
        clas = input('Enter class')

        query = "insert into admission(adno, rno, sname, address, phon, clas) values('{}', {}, '{}', '{}', '{}', '{}')".format(adno, rno, sname, address, phon, clas)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('Record has been saved in admission table')
    except:
        print('error')

def show_admn_details():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    cursor.execute("select * from admission")
    data = cursor.fetchall()
    for row in data:
        print(row)

def search_admn_details():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Admission Number')
    st = "select * from admission where adno='%s'" % (ac)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)

def delete_admn_details():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Admission no')
    st = "delete from admission where adno='%s'" % (ac)
    cursor.execute(st)
    mycon.commit()
    print('Data deleted successfully')

def edit_admn_details():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()

    print("1: Edit name")
    print("2: Edit Address")
    print("3: Phone number")
    print("4: Return")
    print("\t\t----------------------------------------------------------")
    choice = int(input("Enter your choice"))
    if choice == 1:
        admission.edit_name()
    elif choice == 2:
        admission.edit_address()
    elif choice == 3:
        admission.edit_phno()
    elif choice == 4:
        return
    else:
        print("Error: Invalid Choice try again.....")
        conti = "Press any key to return to "

def edit_name():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Admission Number')
    nm = input('Enter correct name')
    st = "update admission set sname='%s' where adno='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

def edit_address():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Admission Number')
    nm = input('Enter correct address')
    st = "update admission set address='%s' where adno='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

def edit_phno():
    mycon = co.connect(host="localhost", user="root", passwd="aarushi9530", database="MPS")
    cursor = mycon.cursor()
    ac = input('Enter Admission Number')
    nm = input('Enter correct phone number')
    st = "update admission set phno='%s' where adno='%s'" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')
