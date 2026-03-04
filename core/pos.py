import file_system

# LOGIN
def login (stored_username , stored_password):
       
    while True: 
        username = input("Enter username: ")
        password = input("Enter 4-digit password: ")

        if username == stored_username and password == stored_password  :
            print("Login successful!")
            print(f"Welcome, {username}\n")
            main_menu()
            break
        
        else:
            print("Invalid username or password.")
            continue

# REGIESTER USER
def register ():

    while True:

        print("--- Register User ---") 
        
        username = input("Enter username: ")
        password = input("Enter 4-digit password: ")
        confirm_password = input("Confirm password: ")

        if len(password) != 4 or password != confirm_password or not password.isdigit():
            print("Wrong password! Try again.")
            continue 
        else:
            print("User created successfully!\n")
            print("Redirecting to login...\n")
            
        break
    return username , password

# MAIN MENU
def main_menu():

    fs = file_system.fs # get object from module

    print("==============================")
    print("           Main Menu          ")
    print("==============================")

    while True:

        print("1. File System")
        print("2. Process Manager")
        print("3. Memory Manager")
        print("4. View Logs")
        print("5. Logout")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid choice type!")

        if choice == 1:
            fs.file_system_menu()

        elif choice == 2:
            pass

        elif choice == 3:
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            print("Back...")
            start_os()
            break

        else:
            print("Invalid choice.")

# PROJECT START FROM HERE
def start_os ():

    stored_username = None
    stored_password = None

    print("==============================")
    print("           PYTHON OS          ")
    print("==============================")

    while True:

        #  Main programs start form here
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        try:    # To avoid user wrong input
            choice = int(input("Choose an option (1-3): "))
        except ValueError: # To void crashes
            print("Invalid choice type.")
            continue

        if(choice == 1):

            if(stored_username == None):
                print("User does not exsist.\n")
            else:
                login(stored_username , stored_password)

        elif(choice == 2):
            stored_username , stored_password = register()
            login(stored_username , stored_password)
        
        elif(choice == 3):
            print("Bye!")
            break
        else:
            print("Invalid choice.")
start_os()