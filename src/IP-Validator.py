import os
import ipaddress
import ctypes
import pyfiglet
import time

ctypes.windll.kernel32.SetConsoleTitleW("IP Validator | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("IP Validator")
print(ascii_banner)

while True:
    ip = input("IP Address to check: ")
    try:
        print(ipaddress.ip_address(ip))
        print("Valid IP")
    except:
        print("-"*79)
        print("NOT Valid IP")
    finally:
        if ip == "q":
            print("Exiting...")
            time.sleep(3)
            exit()