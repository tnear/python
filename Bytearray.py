# A bytearray is a mutable sequence of integers in range [0, 255]

import string

def convert():
    nums = [3, 1, 2]
    byte_array = bytearray(nums)
    assert byte_array == b'\x03\x01\x02'

def create():
    # create 8 null bytes
    buffer = bytearray(8)
    buffer[0] = ord('h')
    buffer[1] = ord('e')
    buffer[2] = ord('l')
    buffer[3] = ord('l')
    buffer[4] = ord('o')

    result = buffer.decode().rstrip('\0')
    assert result == 'hello'

def decode_ascii():
    mixed_data = b'Hello,\x00World!\x1F\x7F\x80\x9F This \x01is\x02 a \x03test.'

    # decode into ascii while ignoring errors
    string_result = mixed_data.decode('ascii', errors='ignore')

    # convert to printable characters
    printable_only = ''.join(char for char in string_result if char in string.printable)
    assert printable_only =='Hello,World! This is a test.'

def main():
    convert()
    create()
    decode_ascii()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
