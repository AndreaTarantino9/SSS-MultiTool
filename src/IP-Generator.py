import random 
import os
import colorama
import ctypes
import pyfiglet

ctypes.windll.kernel32.SetConsoleTitleW("IP Generator | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("IP Generator")
print(ascii_banner)

print("How many IPs do you want to generate?")
num = int(input(">: "))

def gen_ip():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip

if __name__ == "__main__":
    num_ips = num

    for i in range(num_ips):
        random_ip = gen_ip()
        print(random_ip)

input("Press ENTER to exit")