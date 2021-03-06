import json

from scanner import scanner
from id_script import identifier

DEV_LIST_LOC = 'dev_list.json'
HOST = '192.168.0.0/24'
VENDORS = ['ecobee']

sc = scanner(HOST)
nmap_dev_list = sc.nmap_list_scan()

dev_list = open(DEV_LIST_LOC, 'w')
dev_list.write(str(nmap_dev_list).replace('\'', '\"').replace('None', '\"None\"')) #for JSON compatibility
dev_list.close()

f = open(DEV_LIST_LOC, 'r')
devices = json.load(f)
f.close()

id1 = identifier(devices, VENDORS)
print(id1.iotid())
