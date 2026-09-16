# zlib — Lossless compression compatible with gzip
# https://docs.python.org/3/library/zlib.html

import zlib

def compress():
    # string to compress
    text = b'my text string to compress, my text string'
    compressed = zlib.compress(text)
    print(f'{len(text)=}')
    print(f'{len(compressed)=}')
    assert len(compressed) < len(text)

    # decompress to retrieve initial data
    decompressed = zlib.decompress(compressed)
    assert text == decompressed

# cyclic redundancy check
def crc32():
    text = b'hello world'
    crc = zlib.crc32(text)
    assert crc == 222957957

def main():
    compress()
    crc32()

if __name__ == '__main__':
    main()
    print('Tests passed!')
