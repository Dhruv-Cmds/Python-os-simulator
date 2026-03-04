import os

class FileSystem:

    # CREAT FILES
    def create_file(self):

        # creat file = cf
        # current support formate .txt
        cf = input("Enter file name (format: .txt): ")

        with open (cf , "w") as f:
            # file content = fc
            fc = input("Enter file content: ")
            f.write(fc)
            print("File created successfully.")

        return cf

    # READ FILES
    def read_file(self, cf):
        if os.path.exists(cf):
            with open(cf, "r") as f:
                print(f.read())
        else:
            print("File not found.")

    # DELETE FILES
    def delete_file(self, cf):

        if os.path.exists(cf):
            os.remove(cf)
            print("File deleted.")
        else:
            print("File not found.")

    # SHOW LIST OF FILES
    def list_file(self):
        
        print("Files:")
        files = [f for f in os.listdir() if f.endswith(".txt")]
        for i , file in enumerate(files , 1):
            print(f"{i}: {file}")

    # MAIN FILE SYSTEM MENU START FORM HERE
    def file_system_menu(self):

        cf = None

        print("--- File System ---")
        
        while True:

            print("1. Create File")
            print("2. Read File")
            print("3. Delete File")
            print("4. List Files")
            print("5. Back")

            try:
                choice = int(input("Choose an option: "))
            except ValueError:
                print("Invalid choice type!")
                continue
            
            if choice == 1:
                self.create_file()

            elif choice == 2:
                file_name = input("Enter file name to read: ")
                self.read_file(file_name)

            elif choice == 3:
                
                file_name = input("Enter file name to delete: ")
                self.delete_file(file_name)

            elif choice == 4:
                self.list_file()

            elif choice == 5:
                print("Back...")
                break

            else:
                print("Invalid choice.")

fs = FileSystem()