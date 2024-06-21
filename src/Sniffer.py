import os
import pyfiglet
import colorama
import ctypes
import time
from scapy.all import *

ctypes.windll.kernel32.SetConsoleTitleW("Sniffer | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("Sniffer")
print(ascii_banner)

a = input("Start sniffing now? (y/n): ")
if a=="y":
    pass
    print("Press CTRL+C to stop sniffing")
    time.sleep(3)
else:
    print("Exiting...")
    time.sleep(3)

while True:
      pkt=sniff(filter='tcp', count=1)
      if 'http' or 'https' in pkt.summary():
          print(pkt.summary())
