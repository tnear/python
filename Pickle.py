import pickle # Converts object into byte stream

class Attack:
    # __reduce__ method defines class pickling behavior
    # Using eval, can arbitrarily call any Python code
    # Therefore, only unpickle data you trust
    # JSON is a safer alternative

    def __reduce__(self):
        return eval, ("print('This has been EVALed!')",)

def dumps():
    # obj <-> bytes (no file)
    d = {'a': 1, 2: 'b'}
    b = pickle.dumps(d) # b'\x80\x04\x95\x11...
    l = pickle.loads(b)
    assert l == d
    print('dumps passed!')

def dump():
    # obj <-> bytes (file)
    # Binary file mode (b) is required

    d = {'a': 1, 2: 'b'}
    with open('myD.bin', 'wb') as f:
        # write binary
        pickle.dump(d, f)

    with open('myD.bin', 'rb') as f:
        # read binary
        l = pickle.load(f)

    assert l == d
    print('dump passed!')

def main():
    dumps()
    dump()

    malicious = pickle.dumps(Attack())
    pickle.loads(malicious)

if __name__ == '__main__':
    main()
