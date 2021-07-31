import nmap3

DEV_LIST_LOC = '../dev_list'
HOST = '192.168.0.0/24'

class scanner:
	def __init__(self, h):
		self.ch_host(h)

	def ch_host(self, h):
		self.host = h

	def nmap_list_scan(self):
		nm = nmap3.Nmap()
		self.scan_results = nm.scan_top_ports(self.host, args="-sn")
		return self.scan_results

sc = scanner(HOST)
nmap_dev_list = sc.nmap_list_scan()

dev_list = open(DEV_LIST_LOC, 'w')
dev_list.write(str(nmap_dev_list))
dev_list.close()
