class identifier:
    def __init__(self, dev_lst, ven_lst):
        self.devices = dev_lst
        self.vendors = ven_lst

    def iotid(self):
        dev_list_ven = []
        for key, value in self.devices.items():
            try:
                dev_list_ven.append({'ip': key, 'vendor': value['macaddress']['vendor']})
            except:
                pass
        dev_list_ven = [i for i in dev_list_ven if i['vendor'] in self.vendors]
        return dev_list_ven
