import re

# mylist = re.findall(<pattern>, <txt>)
def findAll():
    txt = 'a11 22b34'
    out = re.findall(r'\d+', txt)
    assert out == ['11', '22', '34']

def sub():
    # replace 'E' registers with 'R':
    txt = 'ex: registers eax, ebx, esi'
    out = re.sub(r'\be(\w\w\b)', r'r\1', txt)
    assert out == 'ex: registers rax, rbx, rsi'

def split():
    txt = 'a_var__ex'
    out = re.split('_+', txt)
    assert out == ['a', 'var', 'ex']

def search():
    # Captures floating point number in capture group
    txt = 'speed: 123.45 elements/s'

    num = re.search(r'speed:\s([\d|\.]+) elements/s', txt)

    assert len(num.groups()) == 1
    captureGroup1 = num.group(1)
    assert captureGroup1 == '123.45'

def main():
    findAll()
    sub()
    split()
    search()

if __name__ == '__main__':
    main()
    print('Tests passed!')
