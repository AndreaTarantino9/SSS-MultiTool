import socket
import os
import threading
from datetime import datetime
from colorama import Fore
import time
import ctypes
import pyfiglet

ctypes.windll.kernel32.SetConsoleTitleW("Port Scanner | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

target= input("Enter target IP: ")

os.system("cls")
print("-"*41)
print("Scanning: " + target)
print("Time started: " + str(datetime.now()))
print("-"*41)

ports = []

def scan(port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.settimeout(1)
    try:
        connection.connect((target, port))
        connection.close()
        print(f"{Fore.WHITE}Port {Fore.RED}[{port}] {Fore.WHITE}is open")
        ports.append(port)
    except:
        pass

scanned = 1
for port in range(1, 65535):
    thread = threading.Thread(target=scan, kwargs={"port":scanned})
    scanned += 1
    thread.start()
print(f"{scanned} ports scanned")
print("Open ports: " + str(ports))

input("Press ENTER to exit")