# ipaddress — IPv4/IPv6 manipulation library
# https://docs.python.org/3/library/ipaddress.html

import ipaddress

def factory():
    # use the ipaddress's factory function to create an IPv4Address object
    ip = ipaddress.ip_address('196.168.0.1')

    assert isinstance(ip, ipaddress.IPv4Address)
    assert ip.is_global

def convert():
    ip = ipaddress.ip_address('196.168.0.1')

    # convert ip address to string
    ipStr = str(ip)
    assert ipStr == '196.168.0.1'

    # convert ip address to integer
    ipInt = int(ip)
    assert ipInt == 3299344385

def main():
    factory()
    convert()

if __name__ == '__main__':
    main()
    print('Tests passed!')
