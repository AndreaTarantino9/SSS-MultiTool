import colorama
import os
import time
import ctypes
import pyfiglet

ctypes.windll.kernel32.SetConsoleTitleW("IP-Pinger | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("IP-Pinger")
print(ascii_banner)

def ipping():
    count = 1
    hostname = input("Enter the IP Address here: ")
    os.system("cls")
    print("-"*100)
    print("="*100)
    print("+"*100)
    while True:
        response = os.system("ping -n 1 " + hostname + ">nul")
        if response == 0:
            print(colorama.Fore.GREEN + "[" + str(count) + "] " + hostname + " is up!")
            count += 1
        else:
            print(colorama.Fore.RED + "[" + str(count) + "] " + hostname + " got down ;) !")
            count += 1
        time.sleep(.5)

ipping()