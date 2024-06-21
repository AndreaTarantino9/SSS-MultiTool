import os
import time
import ctypes
import colorama
import pyfiglet
import whois

ctypes.windll.kernel32.SetConsoleTitleW("WhoIS Lookup | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("WhoIS")
print(ascii_banner)

def is_registered(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

domain_name = input("Domain name: ")
if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    print("Domain registrar:", whois_info.registrar)
    print("WHOIS server:", whois_info.whois_server)
    print("Domain creation date:", whois_info.creation_date)
    print("Expiration date:", whois_info.expiration_date)
    print(whois_info)

input("Press ENTER to exit")