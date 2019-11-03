#!/bin/python3
#by Qzacy

import requests
import json
import sys

def locate():
    data = requests.get("http://ip-api.com/json/" + ip + "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy")
    resp = data.json()
    print("\nResults:\n")
    print("Status: " + resp["status"])
    if resp["status"] == "fail":
        print("E-Message: " + resp["message"])
        sys.exit()
    print("Continent: " + resp["continent"])
    print("Continent Code: " + resp["continentCode"])
    print("Country: " + resp["country"])
    print("Country Code: " + resp["countryCode"])
    print("Region: " + resp["region"])
    print("Region Name: " + resp["regionName"])
    print("City: " + resp["city"])
    print("District: " + resp["district"])
    print("Zip: " + resp["zip"])
    print("Latitude: " + str(resp["lat"]))
    print("Longitude: " + str(resp["lon"]))
    print("Timezone: " + resp["timezone"])
    print("Currency: " + resp["currency"])
    print("ISP: " + resp["isp"])
    print("ORG: " + resp["org"])
    print("AS: " + resp["as"])
    print("AS Name: " + resp["asname"])
    print("Reverse: " + resp["reverse"])
    print("Mobile: " + str(resp["mobile"]))
    print("Proxy: " + str(resp["proxy"]))

print("Welcome to geoIp, coded by Qzacy.")
ip = input("Enter the website name or the ip:\ngeoIp > ")
locate()