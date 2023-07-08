# zlib — Lossless compression compatible with gzip
# https://docs.python.org/3/library/zlib.html

import zlib

def compress():
    # string to compress
    text = b'my text string to compress, my text string'
    data = zlib.compress(text)
    assert len(data) < len(text)

    # decompress to retrieve initial data
    decompressed = zlib.decompress(data)
    assert text == decompressed

def main():
    compress()

if __name__ == '__main__':
    main()
    print('Tests passed!')
