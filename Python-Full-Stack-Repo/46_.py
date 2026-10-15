# Student management CRUD operation code 
student = []
while True:
    print("press 1 to Create Account  ")
    print("2 to view details ")
    print("3 to update account details ")
    print("4 to delete account ")
    print("5 to search  ")
    print("6 to exit ")
    choice = int(input("Enter your choice"))
    match(choice):
        case 1:
            rollno = int(input("Enter your roll no "))
            name = input("Enter your name ")
            age = int(input("Enter your age "))
            marks = int(input("Enter your marks "))
            city = input("Enter your city ")
            student.append([rollno,name,age,marks,city])
        case 2: 
            for i in student:
                print(i)
        case 3:
            
            roll_no = int(input("Enter roll no to update "))
            for i in student:
                if(i[0] == roll_no):
                    i[1] = input("Enter Your name ")
                    i[2] = int(input("Enter your age "))
                    i[3] = int(input("Enter your marks "))
                    i[4] = input("Enter your city ")
            print("Values updated sucessfully ")


        case 4:
            for i in student:
                student.remove(i)
        case 5:
            element = int(input("Enter roll no to search"))
            for i in student:
                if(i[0] == element ):
                    print("Element is found at index ")
                else:
                    print("Not present in the list ")

        case 6:
            break 
    