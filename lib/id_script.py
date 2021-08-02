import json
DEV_LIST_LOC = './dev_list.json'
VENDORS = ['ecobee']


class identifier:
    def __init__(self, dev_lst, ven_lst):
        self.devices = dev_lst
        self.vendors = ven_lst

    def iotid(self):
        dev_list_ven = []
        for key, value in dev_list.items():
            try:
                dev_list_ven.append({'ip': key, 'vendor': value['macaddress']['vendor']})
            except:
                pass
        dev_list_ven = [i for i in dev_list_ven if i['vendor'] in self.vendors]
        return dev_list_ven


f = open(DEV_LIST_LOC, 'r')
dev_list = json.load(f)
f.close()

id1 = identifier(dev_list, VENDORS)
print(id1.iotid())
