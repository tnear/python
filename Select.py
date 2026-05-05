'''
select - Waiting for I/O completion
https://docs.python.org/3/library/select.html
'''

import select
import socket

def basic_usage():
    HOST = "127.0.0.1"
    PORT = 5000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    server.setblocking(False)

    print(f"Listening on {HOST}:{PORT}")
    print("Now, in another terminal, run:")
    print(f"$ nc {HOST} {PORT}")
    print()

    timeout_sec = 10

    # select.select() is the interface to the Linux select() syscall.
    # It accepts file descriptors and returns 3 lists which are
    # subsets of the input arguments.
    # Example below returns a readable list (write/except not used)
    readable_list = [server]
    writable_list = []
    exceptional_list = []
    readable, _, _ = select.select(readable_list, writable_list, exceptional_list, timeout_sec)

    if not readable:
        print("No client connected within 10 seconds.")
    else:
        conn, addr = server.accept()
        conn.setblocking(True)
        print(f"Accepted connection from {addr}")

        data = conn.recv(1024)
        print(f"Received: {data!r}")

        conn.sendall(b"Hello from select demo\n")
        conn.close()

    server.close()

def main():
    basic_usage()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
