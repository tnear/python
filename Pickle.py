# pickle — Python object serialization
# https://docs.python.org/3/library/pickle.html

import pickle  # Converts object into byte stream
import pathlib

class Attack:
    # __reduce__ method defines class pickling behavior
    # Using eval, can arbitrarily call any Python code
    # Therefore, only unpickle data you trust
    # JSON is a safer alternative

    def __reduce__(self):
        return eval, ("print('Security issue: this has been EVALed!')",)

def dumps():
    # obj <-> bytes (no file)
    d = {'a': 1, 2: 'b'}
    b = pickle.dumps(d) # b'\x80\x04\x95\x11...
    l = pickle.loads(b)
    assert l == d

def dump():
    # obj <-> bytes (file)
    # Binary file mode (b) is required

    file = 'myD.bin'
    d = {'a': 1, 2: 'b'}
    with open(file, 'wb') as f:
        # write binary
        pickle.dump(d, f)

    with open(file, 'rb') as f:
        # read binary
        l = pickle.load(f)

    assert l == d
    # cleanup
    pathlib.Path(file).unlink()

def main():
    dumps()
    dump()

    malicious = pickle.dumps(Attack())
    pickle.loads(malicious)

if __name__ == '__main__':
    main()
    print('Tests passed!')
