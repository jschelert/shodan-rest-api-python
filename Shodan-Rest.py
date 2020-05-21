import shodan
import requests
import json
import time
from csv import reader

# Defines Variable for Current Time and Appends Shodan for File Creation
current_time = str(time.time())
("shodan", current_time + '.txt')

#Shodan API Key
SHODAN_API_KEY = "" 
api = shodan.Shodan(SHODAN_API_KEY)

#Definte any facets
FACETS = ""

#Ports string variable
PORT ="Port:3389"

# Open File Shodan and writes via the json.dump method
with open(('shodan' + current_time + '.txt') , "w") as outfile:
    #Opens file of FQDN Suffixes
        with open('C:\python38\\fdqn.txt', 'r') as f:
                for line in f:
                    line = line.strip()
                    SEARCH = "ssl.cert.subject.cn:" + line + ' ' + PORT
                    print (SEARCH)
                    searchResolve = 'https://api.shodan.io/shodan/host/search?' + '&key=' + SHODAN_API_KEY + '&query=' + SEARCH + '&facets' + FACETS
                    resolved = requests.get(searchResolve)
                    jsonResponse = resolved.json()
                    json.dump(jsonResponse, outfile, ensure_ascii=False, indent=4)
                    time.sleep(2)

