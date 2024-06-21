import os
import colorama
import ctypes
import pyfiglet
import socket as s
import sys

ctypes.windll.kernel32.SetConsoleTitleW("Website IP | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("Website IP")
print(ascii_banner)

host = input("Website: ")
print (f'IP of {host} is {s.gethostbyname(host)}')
input("Press ENTER to exit")