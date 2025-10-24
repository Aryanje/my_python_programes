print(" _________________________________________________")
print("\n *****WELCOME TO STUDENT MANAGEMENT SYSTEM*****")
sms = open("sdata.txt", "a+")

def showname():
    sms= open("sdata.txt","r")
    for i in sms:
        print(i)
    sms.close()

def addname():
    sms = open("sdata.txt","a+")
    name = input("Enter New Name :")
    name = name+"\n"
    sms.write(name)
    print("Student name added succussfully")
    sms.close()

def removename():
    sms = open("sdata.txt","a+")
    name = input("Remove Student name :")
    name = name+"\n"
    sms.seek(0)
    rn = sms.readlines()
    if name in rn:
        rn.remove(name)
        print("Student name removed",name)
        s = ""
        s = "".join([str(i) for i in rn])
        f1 = open("sdata.txt","w")
        f1.write(s)
        f1.close()
    else:
        print("Name not found")
    sms.close()


def searchname():
    sms = open("sdata.txt","r")
    name = input("Search Student Name :")
    readfile = sms.read()
    if name in readfile:
        print("Student Name found :",name)
    else:
        print("Student Not Found")
    sms.close()

while True:
    try:
    
        print("__________________________")
        print("Please chose any one option")
        print("1. To View Student List")
        print("2. To Add New List")
        print("3. To Remove Student Name from List")
        print("4. To Search Student Name")
        print("5. Exit")
        ch = int(input("Enter Your Choice (1- 5) :"))
        if ch == 1:
            showname()
        elif ch== 2:
            addname()
        elif ch== 3:
            removename()
        elif ch == 4:
            searchname()
        elif ch== 5:
            exit()
        else:
            print("Wrong Entry")
        c=input("Do you want to continue...(y/n):")
        if c=="y":
            continue
        elif c=="n":
            break
    except ValueError:
        print("Invalid input, Please Enter valid option")


















                    
        
    
    
    
    

