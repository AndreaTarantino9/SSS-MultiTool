import os
import pyfiglet
import ctypes
import requests

ctypes.windll.kernel32.SetConsoleTitleW("Webhook Spammer | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("Webhook Spammer")
print(ascii_banner)

webhook = input("\nWebhook: ")
message = input("\nMessage: ")
count = int(input("\nCount: "))

for i in range(count):
    requests.post(webhook, json={"content": message})
    print("Sent: " + str(i + 1))