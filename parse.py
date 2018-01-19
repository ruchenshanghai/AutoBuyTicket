import re
from pprint import pprint

with open('stations.txt', 'r') as f:
    text = f.read().decode('utf-8')
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', text)
    dicRes = dict(stations)
    # pprint(dicRes, indent=4)
    print "["
    for (d, x) in dicRes.items():
        print "{ \"name\":\"" + d + "\", \"code\": \"" + (d + "," + x) + "\"},"
    print "]"