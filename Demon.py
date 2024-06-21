import colorama
import ctypes
import os
import pyfiglet

ctypes.windll.kernel32.SetConsoleTitleW("Demon | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("Demon")
print(ascii_banner)

print("Welcome to Demon. Type Help if you're a beginner.")
choice = input("\n> ")

if choice=="Help" or choice=="help" or choice=="HELP":
    print("\n  Ping                check if your target is online.")
    print("  PScanner            scan for open ports.")
    print("  WebIP               get the IP of a website.")
    print("  IPinfo              get information about an IP address.")
    print("  Sniffer             sniff traffic.")
    choice = input("\n> ")
elif choice=="Ping" or choice=="ping" or choice=="PING":
    os.system("py src/IP-Pinger.py")

elif choice=="PScanner" or choice=="pScanner" or choice=="PSCANNER" or choice=="pscanner" or choice=="Pscanner":
    os.system("py src/Port-Scanner.py")

elif choice=="WebIP" or choice=="webIP" or choice=="WEBIP":
    os.system("py src/Website-IP.py")

elif choice=="IPinfo" or choice=="ipinfo" or choice=="IPINFO":
    os.system("py src/IP-Info.py")

elif choice=="Sniffer" or choice=="sniffer" or choice=="SNIFFER":
    os.system("py src/Sniffer.py")

else:
    print("Invalid command. Type Help if you're a beginner.")