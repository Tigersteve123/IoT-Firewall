from scanner import scanner

DEV_LIST_LOC = 'dev_list.json'
HOST = '192.168.0.0/24'

sc = scanner(HOST)
nmap_dev_list = sc.nmap_list_scan()

dev_list = open(DEV_LIST_LOC, 'w')
dev_list.write(str(nmap_dev_list).replace('\'', '\"').replace('None', '\"None\"')) #for JSON compatibility
dev_list.close()
