#!/usr/bin/python3

import json
import os
import re
import sys

if len(sys.argv) != 2:
    raise ValueError('Please provide a mode parameter (smart|temp)')

mode = sys.argv[1]

disks = []
for root, dirs, files in os.walk('/var/local/snmp'):
    for file in files:
        data = {
                'channel': "-".join(file.split('-')[2:])
        }
        with open(os.path.join(root, file)) as lines:
            for line in lines:
                if mode == 'temp':
                    temp = re.findall(r'^Current Drive Temperature:.*', line)
                    if len(temp) > 0:
                        data['value'] = temp[0].split(' ')[7] #Disk temp
                if mode == 'smart':
                    smart = re.findall(r'^SMART Health Status:.*', line)
                    if len(smart) > 0:
                        data['value'] =(1 if smart[0].split(' ')[3] == "OK" else 2) #Disk health
        
        disks.append(data)

print(json.dumps({
    "prtg": {
        "result": [disk for disk in disks if 'value' in disk and 'channel' in disk]
    }    
}))
