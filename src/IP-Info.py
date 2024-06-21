import os
import ctypes
import colorama
import pyfiglet
from urllib.request import urlopen
import json

ctypes.windll.kernel32.SetConsoleTitleW("IP-Info | Tarantino Andrea")
os.system("color 4")
os.system("cls")

ascii_banner = pyfiglet.figlet_format("IP-Info")
print(ascii_banner)

while True:
    ip = input("\nWhat is your target IP: ")
    url = "http://ip-api.com/json/"
    response = urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print("\nIP: " + values["query"])
    print("City: " + values["city"])
    print("Region: " + values["region"])
    print("Country: " + values["country"])
    print("ISP: " + values["isp"])
    print("Org: " + values["org"])
    print("Zip: " + values["zip"])
    print("Timezone: " + values["timezone"])
    print("Hosting: " + values["as"])
    print("Country code: " + values["countryCode"])
