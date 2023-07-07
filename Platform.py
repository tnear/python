# platform — Access to underlying platform’s identifying data
# https://docs.python.org/3/library/platform.html

import platform

def architecture():
    # Returns tuple of (bits, linkage)
    arch = platform.architecture()
    assert arch == ('64bit', 'WindowsPE')

def machine():
    # Returns machine type
    m = platform.machine()
    assert m == 'AMD64'

def node():
    # Returns computer name (hostname)
    n = platform.node()
    assert 'LAPTOP' in n

def platformFcn():
    # Return human readable description of platform
    p = platform.platform()
    assert 'Windows' in p

def processor():
    p = platform.processor()
    assert p == 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel'

def release():
    # Returns system's release
    r = platform.release()
    assert r == '10'

def system():
    # Return OS name
    # value = {ispc: 'Windows', islinux: 'Linux', ismac: 'Darwin'}
    s = platform.system()
    assert s == 'Windows'

def version():
    v = platform.version()
    assert v == '10.0.19044'

def uname():
    # Returns 6 other platform attributes at once:
    # 1. system, 2. node, 3. release, 4. version, 5. machine, 6. processor
    u = platform.uname()
    assert len(u) == 6

def main():
    architecture()
    machine()
    node()
    platformFcn()
    processor()
    release()
    system()
    version()
    uname()

if __name__ == '__main__':
    main()
    print('Tests passed!')
