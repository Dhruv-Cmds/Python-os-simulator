#  FILE SYSTEM
import os
from logger import log

BASE_DIR = "data/files"

class FileSystem:

    # CREAT FILES
    def create_file(self):

        # creat file = cf
        cf = input("Enter file name: ").strip()

        if "." not in cf:
            cf += ".txt"
        
        else:
            name , ext = cf.rsplit("." , 1)
            cf = name + "." + ext.lower()
        
        # blocked types:

        blocked = [".mp3" , ".mp4" , ".png" ,
                   ".jpg" , ".jpeg" , ".exe" , 
                   ".dll" , ".zip" , ".rar" , 
                   ".iso"]
        
        if any(cf.endswith(ext) for ext in blocked):
            print("Unsupported file type for this system.")
            return
        
        path = os.path.join(BASE_DIR, cf)

        if os.path.exists(path):
            print("File already exists.")
            return
        
        lines = []

        while True:

            # file content = fc
            fc = input("Enter file content (type 'Q' to finish):  ").capitalize()
            
            if fc == "Q":
                break
            lines.append(fc)
        
        content = "\n".join(lines)

        with open(path , "w") as f:
            f.write(content)
        print("File created successfully.")

        log(f"File {cf} created")

        return cf

    # READ FILES
    def read_file(self, cf):

        path = os.path.join(BASE_DIR, cf)

        if os.path.exists(path):
            with open(path, "r") as f:
                print(f.read())

            log(f"File {cf} read")

        else:
            print("File not found.")

    # DELETE FILES
    def delete_file(self, cf):

        path = os.path.join(BASE_DIR, cf)

        if os.path.exists(path):
            os.remove(path)
            print("File deleted.")

            log(f"File {cf} deleted")

        else:
            print("File not found.")

    # SHOW LIST OF FILES
    def list_file(self):
        
        print("Files:")
        files = os.listdir(BASE_DIR)
        for i , file in enumerate(files , 1):
            print(f"{i}: {file}")

        log("File list viewed")

    # MAIN FILE SYSTEM MENU START FORM HERE
    def file_system_menu(self):

        cf = None

        print("\n--- File System ---")
        
        while True:

            print("1. Create File")
            print("2. Read File")
            print("3. Delete File")
            print("4. List Files")
            print("5. Back")

            try:            # To avoid user wrong input
                choice = int(input("Choose an option: "))
            except ValueError:     # To void crashes
                print("Invalid choice type!")
                continue
            
            if choice == 1:
                self.create_file()

            elif choice == 2:
                file_name = input("Enter file name to read: ")
                self.read_file(file_name)

            elif choice == 3:
                
                file_name = input("Enter file name to delete: ")
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() != "y":
                    return
                self.delete_file(file_name)

            elif choice == 4:
                self.list_file()

            elif choice == 5:
                print("Back...")
                break

            else:
                print("Invalid choice.")

fs = FileSystem()