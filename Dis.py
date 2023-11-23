# dis - Disassembler for Python bytecode
# https://docs.python.org/3/library/dis.html

import dis

'''
Executing Python code happens in 4 stages:
1. Lexing:
2. Parsing:      Lexing & parsing transform source code into an AST
3. Compiling:    Turning AST into a code object
4. Interpreting: Running the code object

Compiling in Python is simpler than in compiled languages. Less work is done
in compilation and therefore more work is done in interpreting.

A Python interpreter is a VM (software which emulates a physical computer) using a stack machine.
The advantage of creating this bytecode is that lexing, parsing, and compiling only
needs to be done once per code object.
'''

def printer():
    arg = 'world'
    print('hello ' + arg)

def fcn():
    out = dis.dis(printer)
    '''
    dis output (with comments)
    Line = line # in original source
    Idx  = index # into bytecode
    Name = human-readable instruction name
    Arg  = arg to instruction
    Hint = hint from compiler
    Line  Idx  Name            Arg    Hint       Comment
    1      0   LOAD_CONST       1     ('world')  # puts 'world' on stack
           2   STORE_FAST       0     (arg)      # pops stack ('world'), stores in 'arg'

    2      4   LOAD_GLOBAL      0     (print)    # looks up 'print' in globals mapping, stores 'print' on stack
           6   LOAD_CONST       2     ('hello ') # puts 'hello ' on stack. stack is now size 2
           8   LOAD_FAST        0     (arg)      # puts arg='world' on stack. stack size=3 => [print]['hello ']['world']
          10   BINARY_ADD                        # binary_add pops 2 items, adds together, places result on stack
                                                 # stack now equals [print]['hello world']
          12   CALL_FUNCTION    1                # pops 1 arg off stack and then calls function. result goes on stack
                                                 # 'print' returns None. stack=[None]
          14   POP_TOP                           # pops None. stack is empty
          16   LOAD_CONST       0     (None)     # puts None on stack. All functions w/o returns implicitly return 'None'
          18   RETURN_VALUE
    '''
    print(out)

def main():
    fcn();

if __name__ == '__main__':
    main()
    print('Tests passed!')
