import re

# List = re.findall(<pattern>, <txt>)
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

def main():
    findAll()
    sub()
    split()

if __name__ == '__main__':
    main()
    print('Tests passed!')