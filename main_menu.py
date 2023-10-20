import main_menu
import admission
import student_data
while True:
    print("\t\t..........................................................")
    print("\t\t*****Welcome To School Management System*****")
    print("\t\t..........................................................")
    print("\n\t\t*****Mao Public School*****")
    print("1:Admission")
    print("2:Student Data")
    print("3:Exit")
    print("\t\t----------------------------------------------------------")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        admission.ADM_MENU()
    elif choice == 2:
        student_data.STU_MENU()
    elif choice == 3:
        break
    else:
        print("Error:Invalid Choice try again.....")
        conti = input("press any key to continue")
