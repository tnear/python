# hashlib — Secure hashes and message digests
# https://docs.python.org/3/library/hashlib.html
import hashlib

def sha256():
    d = hashlib.sha256(b'my msg').hexdigest()
    assert d == '9ef41c3677182e1e325e4e8a3316cd77cabff57bdbb64bc04f206cbfefebb6df'

def sha256_long():
    m = hashlib.sha256()
    m.update(b'my msg')
    d = m.hexdigest()
    assert d == '9ef41c3677182e1e325e4e8a3316cd77cabff57bdbb64bc04f206cbfefebb6df'

def main():
    sha256_long()
    sha256()

if __name__ == '__main__':
    main()
    print('Tests passed!')
