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
    # Representation: turn object into string for debugging
    # (very similar to str())
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
    # verify last 5 characters:
    assert s[-N:] == 'fghij'

def formattedStringLiteral():
    # aka f-string (string interpolation)

    apples = 4
    bananas = 3

    # Prefix string with 'f' to create an f-string.
    # The string is interpolated using {var}:
    s = f'I have {apples} apples and {bananas} bananas'
    assert s == 'I have 4 apples and 3 bananas'

def fstringFormat():
    value = 1 / 3
    # use colon followed by formatting (.3f = floating point with 3 digits)
    s = f'Value with 3 digits is: {value:.3f}'
    assert s == 'Value with 3 digits is: 0.333'

def strip():
    txt = '  abc  '
    txt = txt.strip()
    assert txt == 'abc'

    # characters parameter
    txt = '!@#$ a...bc! !'

    # strips ALL of these characters from beginning/end
    txt = txt.strip(' $#@!')
    assert txt == 'a...bc'

def find():
    s = 'hello'

    # get first 'l' index
    idx = s.find('l')
    assert idx == 2

    # get first 'el' index
    idx = s.find('el')
    assert idx == 1

    # non-existent substring
    idx = s.find('qqq')
    assert idx == -1

    # start searching at specified index
    s = '::abc::def'
    start = 1
    # start searching at idx=1
    idx = s.find(':', start)
    assert idx == 1

def capitalization():
    s = 'Hello'
    assert s.upper() == 'HELLO'
    assert s.lower() == 'hello'

    # capitalize first letter
    s = 'hello world'
    s = s.capitalize()
    assert s == 'Hello world'

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
    formattedStringLiteral()
    fstringFormat()
    strip()
    find()
    capitalization()

if __name__ == '__main__':
    main()
    print('Tests passed!')
