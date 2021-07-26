import nmap3

DEV_LIST_LOC = '../dev_list'

nm = nmap3.Nmap()

results = nm.nmap_list_scan(host)

dev_list = open(DEV_LIST_LOC, 'w')
dev_list.write(results)
dev_list.close()
