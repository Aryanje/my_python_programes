# Print a welcome banner for the program
print(" _________________________________________________")
print("\n *****WELCOME TO STUDENT MANAGEMENT SYSTEM*****")

# Open the file in append+read mode. If the file doesn't exist, it will be created.
sms = open("sdata.txt", "a+")

# Function to show all student names from the file
def showname():
    sms = open("sdata.txt","r")   # Open file in read mode
    for i in sms:                 # Loop through each line in the file
        print(i)                  # Print each student name
    sms.close()                   # Close the file after reading

# Function to add a new student name
def addname():
    sms = open("sdata.txt","a+")  # Open file in append mode to add new data
    name = input("Enter New Name :")  # Take student name input from user
    name = name+"\n"                  # Add newline so each name is on a new line
    sms.write(name)                   # Write the name into the file
    print("Student name added successfully")  # Confirmation message
    sms.close()                       # Close the file

# Function to remove a student name from the file
def removename():
    sms = open("sdata.txt","a+")      # Open file in append+read mode
    name = input("Remove Student name :")  # Input name to remove
    name = name+"\n"                       # Add newline to match file format
    sms.seek(0)                            # Move cursor to beginning of file
    rn = sms.readlines()                   # Read all lines into a list
    
    if name in rn:                         # Check if the name exists in file
        rn.remove(name)                    # Remove the name from the list
        print("Student name removed",name) # Confirmation message
        
        s = ""                             # Create empty string
        s = "".join([str(i) for i in rn])  # Convert list back to string
        
        f1 = open("sdata.txt","w")         # Open file in write mode (overwrite)
        f1.write(s)                        # Write updated data back to file
        f1.close()                         # Close the file
    else:
        print("Name not found")            # If name doesn't exist
    
    sms.close()                            # Close original file

# Function to search a student name
def searchname():
    sms = open("sdata.txt","r")            # Open file in read mode
    name = input("Search Student Name :")  # Input name to search
    readfile = sms.read()                  # Read entire file content
    
    if name in readfile:                   # Check if name exists in file
        print("Student Name found :",name) # Display found message
    else:
        print("Student Not Found")         # Display not found message
    
    sms.close()                            # Close the file

# Infinite loop to keep the program running until user exits
while True:
    try:
        print("__________________________")
        print("Please choose any one option")
        print("1. To View Student List")
        print("2. To Add New List")
        print("3. To Remove Student Name from List")
        print("4. To Search Student Name")
        print("5. Exit")
        
        ch = int(input("Enter Your Choice (1- 5) :"))  # Take menu choice from user
        
        if ch == 1:
            showname()      # Call function to display student names
        elif ch == 2:
            addname()       # Call function to add a new student
        elif ch == 3:
            removename()    # Call function to remove a student
        elif ch == 4:
            searchname()    # Call function to search a student
        elif ch == 5:
            exit()          # Exit the program
        else:
            print("Wrong Entry")  # Handle invalid menu choice
        
        # Ask user if they want to continue
        c = input("Do you want to continue...(y/n):")
        
        if c == "y":
            continue        # Continue program loop
        elif c == "n":
            break           # Exit loop and stop program
    
    except ValueError:
        # Handle error if user enters non-numeric input
        print("Invalid input, Please Enter valid option")
