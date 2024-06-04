from ipaddress import *

net = ip_network('235.86.56.0/255.255.248.0', 0)

print(sum(1 for ip in net if f'{ip:b}'[-2:] == '11'))