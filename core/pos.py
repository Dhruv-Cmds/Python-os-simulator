import file_system
import process
import memory
from logger import log

class Login:

    # LOGIN
    def login(self , stored_username , stored_password):
        
        while True: 
            username = input("Enter username: ")
            password = input("Enter 4-digit password: ")

            try:
                with open("data/users.txt" , "r") as f:
                    for line in f:
                        u , p = line.strip().split(":")
                        if u == username and p == password:
                            print("Login successful!")
                            print(f"Welcome, {username}\n")

                            log(f"User {username} logged in")

                            l.main_menu()
                            return
            except FileNotFoundError:
                print("No users registered yet.")
                return

            print("Invalid username or password.")
            log(f"Failed login attempt for {username}")

    # REGISTER USER
    def register(self):

        while True:

            print("--- Register User ---") 
            
            username = input("Enter username: ")
            password = input("Enter 4-digit password: ")
            confirm_password = input("Confirm password: ")

            if len(password) != 4 or password != confirm_password or not password.isdigit():
                print("Wrong password! Try again.")
                continue 

            with open("data/users.txt" , "a") as f:
                f.write(f"{username}:{password}\n")

            print("User created successfully!\n")
            print("Redirecting to login...\n")

            log(f"New user registered: {username}")
                
            break

        return username , password

    # MAIN MENU RUN AFTER COMPLETE LOGIN
    def main_menu(self):

        fs = file_system.fs
        p = process.p
        m = memory.m

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
                continue

            if choice == 1:
                fs.file_system_menu()

            elif choice == 2:
                p.process_manager()

            elif choice == 3:
                m.memory_menu()

            elif choice == 4:

                print("\n--- System Logs ---")

                try:
                    with open("data/logs.txt") as f:
                        print(f.read())
                except FileNotFoundError:
                    print("No logs found.")

            elif choice == 5:
                print("Logged out.")
                log("User logged out")
                break

            else:
                print("Invalid choice.")

l = Login()