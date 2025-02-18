# platform — Access to underlying platform’s identifying data
# https://docs.python.org/3/library/platform.html

import platform

def architecture():
    # Returns tuple of (bits, linkage)
    arch = platform.architecture()
    assert '64bit' in arch

def machine():
    # Returns machine type
    m = platform.machine()
    assert m in ('AMD64', 'arm64')

def node():
    # Returns computer name (hostname)
    node = platform.node()
    print(f'{node}')

def platformFcn():
    # Return human readable description of platform
    p = platform.platform()
    assert 'Windows' in p or 'macOS' in p

def processor():
    processor = platform.processor()
    assert 'Intel64' in processor or processor == 'arm'

def release():
    # Returns system's release
    release = platform.release()
    print(f'{release=}')

def system():
    # Return OS name
    # value = {ispc: 'Windows', islinux: 'Linux', ismac: 'Darwin'}
    system = platform.system()
    assert system in ('Windows', 'Darwin')

def version():
    version = platform.version()
    assert 'Version' in version

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
