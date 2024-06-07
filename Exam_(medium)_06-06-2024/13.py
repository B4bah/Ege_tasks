from ipaddress import *

for a in range(0, 256):
    net = ip_network(f'223.167.{a}.167/255.255.255.192', 0)
    if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0') for ip in net):
        if not (ip_address(f'223.167.{a}.167') in (net.network_address, net.broadcast_address)):
            print(a)