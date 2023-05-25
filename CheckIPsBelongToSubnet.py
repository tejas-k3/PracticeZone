# Question : For given subnet IP & List of IP Addresses
# return boolean for each IP Address if it belongs to that
# subnet or not. Example I/O : subnet_ip = '192.168.0.0/24'
# ipList = ['192.168.0.1', '192.168.0.2', '192.168.1.1']

# Assumption :
# 1. Given IPs & Subnets are always valid.
# 2. All IPs (including lowest value & highest value) are valid.

def isIPPartOfSubnet(ip, subnet):
    ipSections = ip.split('.')
    ipBinary = ''.join(format(int(part), '08b') for part in ipSections)
    subnetAddress, prefixLength = subnet.split('/')
    prefixLength = int(prefixLength)
    subnetSections = subnetAddress.split('.')
    subnetBinary = ''.join(format(int(part), '08b') for part in subnetSections)
    ipNetwork = ipBinary[:prefixLength]
    subnetNetwork = subnetBinary[:prefixLength]
    return ipNetwork == subnetNetwork

"""
Example Usage :
subnet = subnet_ip = '192.168.0.0/24'
ipList = ['192.168.0.1', '192.168.0.2', '192.168.1.1']
for ip in ipList:
    print(ip, end='')
    print(isIPPartOfSubnet(ip, subnet))
"""