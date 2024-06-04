from ipaddress import *
#
# for a in range(8, 17):
#     # if not (ip_address('99.8.254.232') in (net.broadcast_address, net.network_address)):
#     net = ip_network(f'99.8.254.232/{a}', 0)
#     if all((f'{ip:b}'[:16].count('1') <= f'{ip:b}'[-16:].count('1')) for ip in net if not (ip in (net.broadcast_address, net.network_address))):
#         print(a)
# net_ = ip_network('99.8.254.232/255.255.248.0', 0)
# if all((f'{ip:b}'[:16].count('1') <= f'{ip:b}'[-16:].count('1')) for ip in net_ if not ):
#     print(net_.netmask)

from fnmatch import *

ip = ip_address('99.8.254.232')
for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   if fnmatch(str(network.netmask), '255.255.*.0'):
       if ip not in [network.network_address, network.broadcast_address]:
           if all(f'{ip:b}'[:16].count('1') <= f'{ip:b}'[16:].count('1')
               for ip in network):
                  print(network.netmask)