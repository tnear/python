# struct — Interpret bytes as packed binary data
# https://docs.python.org/3/library/struct.html

import struct

def pack():
    # struct.pack(formatString, arg1, arg2, ...)
    # ?: bool (1 byte)
    # b: char (1 byte)
    # B: uchar (1 byte)
    # h: short (2 bytes)
    # H: ushort (2 bytes)
    # i: int (4 bytes)
    # I: uint (4 bytes)
    # f: float (4 bytes)
    # d: double (8 bytes)
    # Q: unsigned long long (8 bytes)

    b = struct.pack('i', 12)
    assert b == b'\x0c\x00\x00\x00'

    b = struct.pack('h?', 2, True)
    assert b == b'\x02\x00\x01'

def unpack():
    # float (including precision loss)
    s = struct.pack('f', 1.23456)
    tup = struct.unpack('f', s)
    assert tup == (1.2345600128173828,)

    # double (no precision loss)
    s = struct.pack('d', 1.23456)
    tup = struct.unpack('d', s)
    assert tup == (1.23456,)

    s = struct.pack('h?', 2, True)
    tup = struct.unpack('h?', s)
    assert tup == (2, True)

def string():
    # assume 32 string max length. Uses syntax '32s'
    my_binary_str = b'my_binary_str'
    packed_string = struct.pack('32s', my_binary_str)

    result = struct.unpack('32s', packed_string)
    result = result[0].decode().rstrip('\0')
    assert result == my_binary_str.decode()

def calcsize():
    # Byte order character
    # @ = native (default)
    # < = little-endian
    # > = big-endian
    format_string = '!BBBBLQ'
    size = struct.calcsize(format_string)
    assert size == 16

def main():
    pack()
    unpack()
    string()
    calcsize()

if __name__ == '__main__':
    main()
    print('Tests passed!')
