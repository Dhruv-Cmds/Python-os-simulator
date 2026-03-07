import os
import time
import file_system
import process
import memory
import folder

class Terminal:
        # ---------------- TERMINAL HELP ---------------- #

    def show_help(self):

        print("\nAvailable Commands:\n")

        print("File System:")
        print(" create_file")
        print(" read_file")
        print(" edit_file")
        print(" delete_file")
        print(" list_files")

        print("\nFolder System:")
        print(" create_folder")
        print(" open_folder")
        print(" delete_folder")
        print(" list_folder")

        print("\nMemory Manager:")
        print(" allocate_memory")
        print(" free_memory")
        print(" show_memory")

        print("\nProcess Manager:")
        print(" start_process")
        print(" kill_process")
        print(" view_process")

        print("\nSystem:")
        print(" view_logs")
        print(" help")
        print(" exit\n")


    # ---------------- TERMINAL MODE ---------------- #

    def run_terminal(self):

        start_time = time.time()

        fs = file_system.fs
        p = process.p
        m = memory.m
        fo = folder.fo

        print("\nMini OS Simulator Terminal")
        print("Type 'help' to see commands\n")
        print("Type 'clear' to clear Terminal\n")
        print("Type 'system_info' to check system information\n")
        print("Type 'about' to check about program information\n")
        print("Type 'uptime' to check OS run time\n")

        while True:

            command = input("OS> ").strip()

            if command == "help":
                self.show_help()

            # ---------------- FILE SYSTEM ---------------- #

            elif command == "create_file":
                fs.create_file()

            elif command == "read_file":
                file = input("Enter file name: ")
                fs.read_file(file)

            elif command == "edit_file":
                file = input("Enter file name: ")
                fs.edit_file(file)

            elif command == "delete_file":
                file = input("Enter file name: ")
                fs.delete_file(file)

            elif command == "list_files":
                fs.list_file()

            # ---------------- FOLDER SYSTEM ---------------- #

            elif command == "create_folder":
                fo.create_folder()

            elif command == "open_folder":
                fo.open_folder()

            elif command == "delete_folder":
                fo.delete_folder()

            elif command == "list_folder":
                fo.list_folder()

            # ---------------- MEMORY SYSTEM ---------------- #

            elif command == "allocate_memory":
                m.allocate_memory()

            elif command == "free_memory":
                m.free_memory()

            elif command == "show_memory":
                m.show_current_memory()

            # ---------------- PROCESS SYSTEM ---------------- #

            elif command == "start_process":
                name = input("Enter process name: ")
                p.start_process(name)

            elif command == "kill_process":
                try:
                    pid = int(input("Enter PID: "))
                    p.kill_process(pid)
                except ValueError:
                    print("Invalid PID")

            elif command == "view_process":
                p.view_running_task()

            # ---------------- LOG SYSTEM ---------------- #

            elif command == "view_logs":

                try:
                    with open("data/logs.txt") as f:
                        print(f.read())
                except FileNotFoundError:
                    print("No logs found.")

            elif command == "exit":
                print("Shutting down OS...")
                break

            # ---------------- OS SHORT-CUTS ---------------- #

            elif command == "clear":
                os.system("cls" if os.name == "nt" else "clear")
            
            elif command == "system_info":

                print("\n=== System Information ===")
                print("OS Name: Python OS Simulator")
                print("Version: 1.1.0")
                print("Language: Python")
                print("Modules Loaded:")
                print("- File System")
                print("- Folder Manager")
                print("- Memory Manager")
                print("- Process Manager")
                print("- Logger")
                print("- Command Terminal")
                print("===========================\n")
            
            elif command == "about":

                print("\n=== About Python OS ===")
                print("Python OS Simulator")
                print("Version: 1.2.0")
                print("Built using Python")
                print("Architecture: Modular CLI System")
                print("Modules:")
                print("- File System")
                print("- Folder Manager")
                print("- Memory Manager")
                print("- Process Manager")
                print("- Logger")
                print("- Command Terminal")
                print("=======================\n")
            
            elif command == "uptime":
                print(f"Uptime: {round(time.time() - start_time,2)} seconds")

            else:
                print("Unknown command. Type 'help'")

tml = Terminal()