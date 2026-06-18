'''
selectors - High-level I/O multiplexing
https://docs.python.org/3/library/selectors.html
'''

import selectors
import socket

# selectors.DefaultSelector is Python's recommended high-level
# I/O multiplexer. It wraps the lower-level select primitives
# and automatically picks the most efficient implementation
# for your platform
g_selector = selectors.DefaultSelector()

def my_accept(sock, _mask):
    conn, addr = sock.accept()
    print(f"accepted {addr}")
    conn.setblocking(False)

    # Watch this socket for read readiness. When it is ready,
    # associate with my_read() callback.
    g_selector.register(conn, selectors.EVENT_READ, my_read)

    # selectors only has 2 constants:
    # EVENT_READ: notify when this object (file) is ready for reading
    # EVENT_WRITE (not shown): notify when this object is ready for writing

def my_read(conn, _mask):
    data = conn.recv(1024)
    if data:
        print(f"received from user: {data!r}")
        conn.sendall(b"echo: " + data)
    else:
        print("closing connection")
        g_selector.unregister(conn)
        conn.close()

def basic_usage():
    HOST = "127.0.0.1"
    PORT = 5001
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    server.setblocking(False)

    # Watch the listening socket server, and when it becomes
    # readable, use my_accept as the handler.
    g_selector.register(server, selectors.EVENT_READ, my_accept)

    print(f"Listening on {HOST}:{PORT}")
    print(f"In another terminal, run: nc {HOST} {PORT}")

    # wait for I/O events forever
    while True:
        # block until at least one registered object is ready
        # key = information about the registered object
        # mask = which event happened (such as read-only)
        for key, mask in g_selector.select():
            # get function callback (either my_accept or my_read in this example)
            callback = key.data

            # run callback. 'fileobj' in this case is the socket.
            callback(key.fileobj, mask)

def main():
    basic_usage()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
