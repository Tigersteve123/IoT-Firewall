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
    sc.nmap_list_scan()
    
def iotid():
    id1.iotid()

parser = argparse.ArgumentParser(description='Set up and configure iotfw', prog='iotfw', allow_abbrev=False)

parser.add_argument('--scan', '-s', action='store_const', const=nmap_list_scan)
parser.add_argument('--id', '-i', action='store_const', const=iotid)

args = parser.parse_args()
