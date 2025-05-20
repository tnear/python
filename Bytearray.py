# A bytearray is a mutable sequence of integers in range [0, 255].

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

def main():
    convert()
    create()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
