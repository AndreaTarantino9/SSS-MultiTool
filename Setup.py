import os
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("SSS Setup | Tarantino Andrea")
os.system("color 4")
os.system("cls")

banner = """
 ____  _____ _____ _   _ ____  
/ ___|| ____|_   _| | | |  _ \ 
\___ \|  _|   | | | | | | |_) |
 ___) | |___  | | | |_| |  __/ 
|____/|_____| |_|  \___/|_|    
     
"""

print(banner)

print("Welcome to SSS Setup. This will install all the dependencies needed for the program to run.")

print("\nDo you want to start the setup now? (y/n)")
a = input("> ")

if a=="y":
    os.system("py -m pip install -r requirements.txt")
    print("Setup complete. You can now run the program.")
else:
    print("Setup aborted. Exiting...")
    time.sleep(3)
    os.system("exit")

print("\nDo you want to start the tool now? (y/n)")
b = input("> ")
if b=="y":
    os.system("py SSS.py")
else:
    print("Exiting...")
    time.sleep(2)
    os.system("exit")
