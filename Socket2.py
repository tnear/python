# This module provides access to the BSD socket interface.
# Note: breakpoints do not function when this file is named Socket.py

import re
import socket
import sys

def ipAddress():
    # get ip address for domain (format: w.x.y.z)
    ip = socket.gethostbyname('www.google.com')

    assert ip.count('.') == 3
    out = re.search(r'\d+\.\d+\.\d+\.\d+', ip)
    assert out is not None

def connect():
    # (default) AF_INET = IPv4
    # (default) SOCK_STREAM =  TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    hostIp = socket.gethostbyname('www.google.com')
    port = 80
    # connect to google on port 80
    s.connect((hostIp, port))

def bind():
    s = socket.socket()
    port = 12345
    # empty address allows server to listen to
    # all requests
    s.bind(('', port))

    s.listen()
    # Establish connection

    #Firewall issues
    #conn, address = s.accept()
    #conn.send('Successfully connected!'.encode())
    #conn.close()

def main():
    ipAddress()
    connect()
    bind()

if __name__ == '__main__':
    main()
    print('Tests passed!')
