import colorama
import ctypes
import os
import pyfiglet

ctypes.windll.kernel32.SetConsoleTitleW("SSS | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("SSS")
print(ascii_banner)

print("Welcome to SSS. Type Help if you're a beginner.")
choice = input("\n> ")

if choice=="Help" or choice=="help" or choice=="HELP":
    print("\n  1)Ping                check if your target is online.")
    print("  2)PScanner            scan for open ports.")
    print("  3)WebIP               get the IP of a website.")
    print("  4)IPinfo              get information about an IP address.")
    print("  5)Sniffer             sniff traffic.")
    print("  6)DDoS                perform a DDoS attack.")
    print("  7)IPGen               generate IP address.")
    print("  8)IPValid             validate an IP address.")
    choice = input("\n> ")
elif str(choice)=="1":
    os.system("py src/IP-Pinger.py")

elif str(choice)=="2":
    os.system("py src/Port-Scanner.py")

elif str(choice)=="3":
    os.system("py src/Website-IP.py")

elif str(choice)=="4":
    os.system("py src/IP-Info.py")

elif str(choice)=="5":
    os.system("py src/Sniffer.py")

elif str(choice)=="6":
    os.system("py src/DDoS.py")

elif str(choice)=="7":
    os.system("py src/IPGenerator.py")

elif str(choice)=="8":
    os.system("py src/IP-Validator.py")

else:
    print("Invalid command. Type Help if you're a beginner.")
    input("Press ENTER to exit")