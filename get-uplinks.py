import requests
import json
import csv
from pprint import pprint
from datetime import datetime

organizationId = ""
url = f"https://api.meraki.com/api/v1/organizations/{organizationId}/devices/uplinks/addresses/byDevice"

API_KEY = input('API-KEY: ')

meraki_header = {"Content-type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": API_KEY}

devices_request = requests.get(url, headers=meraki_header, timeout=30)
devices = devices_request.json()

filename = f"DNS-Servere-{datetime.now().strftime('%d%m%Y-%H%M%S')}"

with open(f"{filename}.csv" , 'w', newline='', encoding='utf-8-sig') as csvfile:
    print(f"Writing DNS servers for uplink to file with name: {filename}")
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(['MAC', 'NAVN', 'DNS Servere'])
    for device in devices:
        device_hostname = device['name']
        device_mac = device['mac']
        for uplink in device['uplinks']:
            for address in uplink['addresses']:
                csvwriter.writerow([device_mac, device_hostname, address['nameservers']['addresses']])

csvfile.close()