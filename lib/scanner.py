import nmap3

class scanner:
	def __init__(self, h):
		self.ch_host(h)

	def ch_host(self, h):
		self.host = h

	def nmap_list_scan(self):
		nm = nmap3.Nmap()
		self.scan_results = nm.scan_top_ports(self.host, args="-sn")
		return self.scan_results

