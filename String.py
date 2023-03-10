# Strings in Python 3 are stored as Unicode

def contains():
    assert 'bc' in 'abcd'
    assert 'q' not in 'abcd'

def slice():
    s = 'string'
    assert s[1:3] == 'tr'
    assert s[:4] == 'stri' # Get chars 0 through (4-1)
    assert s[3:] == 'ing'
    assert s[-1] == 'g'
    assert s[-2:] == 'ng'
    assert s[-4:-2] == 'ri'

def reverse():
    # [start : stop : stride]
    # start and stop omitted to get whole string
    # -1 walks backward
    assert 'abc'[::-1] == 'cba'

    # Start at -1 ('c')
    # Go to -4 (one past -3 which is 'a')
    # Use -1 stride to walk backward
    assert 'abc'[-1:-4:-1] == 'cba'

def Format():
    a = 10
    b = '1 to {}!'
    assert b.format(a) == '1 to 10!'

    s = 'Car: {car}, Model: {model}'
    s = s.format(car='Ford', model='F150')
    assert s == 'Car: Ford, Model: F150'

def Hex():
    assert '\x41\x41\x5f' == 'AA_'

def join():
    ip = ['1', '2', '3']
    out = ','.join(ip)
    assert out == '1,2,3'

def hexToInt():
    assert int('deadbeef', 16) == 3735928559

def intToHexToString():
    d = 140714483833450346658229863
    hex1 = format(d, 'x')
    s = bytes.fromhex(hex1).decode()
    assert s == 'test string'

    # 0x6e69622f == 1852400175
    # Reverse string due to little-endian arch
    b = bytes.fromhex('6e69622f')[::-1]
    assert b == b'/bin'
    s = chr(0x2f) + chr(0x62) + chr(0x69) + chr(0x6e)
    assert s == '/bin'

def stringToHexToInt():
    hex1 = b'test string'.hex()
    d = int(hex1, 16)
    assert d == 140714483833450346658229863

    hex1 = format(d, 'x')
    s = bytes.fromhex(hex1).decode()
    assert s == 'test string'

    # reverse '/bin' and convert to hex
    assert b'/bin'[::-1].hex() == '6e69622f'

def encode():
    assert 'abc'.encode() == b'abc'
    assert 'pythön!'.encode() == b'pyth\xc3\xb6n!'

def decode():
    assert b'pyth\xc3\xb6n!'.decode() == 'pythön!'

def Repr():
    # "Representation.
    # Turn object into string for debugging
    # (very similar to str())"
    assert repr([1, 2, 3]) == '[1, 2, 3]'

def replace():
    # replace substring
    s = 'string'
    out = s.replace('str', 'fl')
    assert out == 'fling'

    # remove substring
    out = s.replace('tr', '')
    assert out == 'sing'

    # remove multiple instances
    s = 'str123ing123'
    out = s.replace('123', '')
    assert out == 'string'

def partition():
    # (prefix, found, suffix)
    # Can be used to implement extractBefore/extractAfter
    s = 'my test string'
    prefix, found, suffix = s.partition('test ')
    assert prefix == 'my '
    assert found == 'test '
    assert suffix == 'string'

def lastNCharacters():
    N = 5
    s = 'abcdefghij'

    # [start at negative N : <empty means go to end> : <stride=1(default)>
    assert s[-N:] == 'fghij'

def main():
    contains()
    slice()
    reverse()
    Format()
    Hex()
    join()
    hexToInt()
    intToHexToString()
    stringToHexToInt()
    encode()
    decode()
    Repr()
    replace()
    partition()
    lastNCharacters()

if __name__ == '__main__':
    main()
    print('Tests passed!')
