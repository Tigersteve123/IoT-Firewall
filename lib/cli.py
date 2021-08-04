import os
import sys
import json
import argparse

from scanner import scanner
from id_script import identifier

DEV_LIST_LOC = 'dev_list.json'
HOST = '192.168.0.0/24'
VENDORS = ['ecobee']

f = open(DEV_LIST_LOC, 'r')
devices = json.load(f)
f.close()

sc = scanner(HOST)
id1 = identifier(devices, VENDORS)

def nmap_list_scan():
    nmap_dev_list = sc.nmap_list_scan()
    dev_list = open(DEV_LIST_LOC, 'w')
    dev_list.write(str(nmap_dev_list).replace('\'', '\"').replace('None', '\"None\"')) #for JSON compatibility
    dev_list.close()
    
def iotid():
    iot_devs = id1.iotid()
    print([i['ip'] for i in iot_devs])
    return [i['ip'] for i in iot_devs]

def lsdev():
    for key, value in devices.items():
        try:
            print('ip: ' + key + '; vendor: ' + value['macaddress']['vendor'])
        except: pass

parser = argparse.ArgumentParser(description='Set up and configure iotfw', prog='iotfw', allow_abbrev=False)

parser.add_argument('-s', '--scan', action='store_true', help='Scan network and write to file')
parser.add_argument('-i', '--id', action='store_true', help='Identify IoT devices')
parser.add_argument('-ld', '--lsdev', action='store_true', help='List all devices')

args = parser.parse_args()

if args.scan:
    nmap_list_scan()
if args.id:
    iotid()
if args.lsdev:
    lsdev()
