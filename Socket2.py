# This module provides access to the BSD socket interface.
# Note: breakpoints do not function when this file is named Socket.py

# socket — Low-level networking interface
# https://docs.python.org/3/library/socket.html

import re
import socket
import time
import threading

def ipAddress():
    # get ip address for domain (format: w.x.y.z)
    ip = socket.gethostbyname('www.google.com')

    assert ip.count('.') == 3
    out = re.search(r'\d+\.\d+\.\d+\.\d+', ip)
    assert out is not None

def connect():
    # (default) AF_INET = IPv4
    # (default) SOCK_STREAM = TCP
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

def start_server():
    s = socket.socket()
    s.bind(('localhost', 0))
    port = s.getsockname()[1]
    s.listen(1)

    def handle():
        conn, addr = s.accept()
        data = conn.recv(1024)
        print(f'Received: {data.decode()}')
        print(f'{len(data)=} bytes')
        conn.send(b'OK')
        conn.close()
        s.close()

    threading.Thread(target=handle, daemon=True).start()
    return port

def test_connection():
    port = start_server()
    time.sleep(0.1)  # Let server start

    client = socket.socket()
    client.connect(('localhost', port))
    client.send(b'Hello')
    response = client.recv(1024)
    client.close()

    print(f'Response: {response.decode()}')
    assert response == b'OK'

def main():
    ipAddress()
    connect()
    bind()
    test_connection()

if __name__ == '__main__':
    main()
    print('Tests passed!')
