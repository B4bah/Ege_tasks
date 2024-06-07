from ipaddress import *

net = ip_network('192.168.156.235/255.255.255.240', 0)

k = 0
for ip in net:
    k += 1
    print(ip)