# pdb — The Python Debugger
# https://docs.python.org/3/library/pdb.html

import pdb

def set_trace():
    z = 26
    # use set_trace (or breakpoint()) to enter the debugger
    #pdb.set_trace()

    # Print variables:
    # (Pdb) print(z)
    # 26
    # (Pdb) p z
    # 26

    # Create variables:
    # (Pdb) y = 25
    # (Pdb) p y
    25

# Same as pdb.set_trace()
def breakpointCommand():
    x = 1
    breakpoint()
    y = 2
    z = x + y
    print(z)
    print('Exiting...')

# Displays stack trace
def where():
    '''
    (Pdb) where
      d:\programming\python\pdb.py(17)<module>()
    -> main()
    d:\programming\python\pdb.py(14)main()
    -> set_trace();
    > d:\programming\python\pdb.py(9)set_trace()->None
    -> pdb.set_trace()
    '''
    ...

# Executes current line and moves to next line.
# Does NOT step into function calls
def next():
    '''
    (Pdb) next
    '''
    ...

# Step into functions called at the current line
def step():
    '''
    (Pdb) step
    '''
    ...

def breakpoints():
    '''
    # Show all breakpoints
    (Pdb) break

    # Break in myfile.py, line number 6
    (Pdb) break myfile.py:6
    '''
    ...

def longlist():
    '''
    # List source code for the current function or frame.
    (Pdb) longlist
    (Pdb) ll  # alias
    23     def breakpointFcn():
    24         x = 1
    25         breakpoint()
    26         y = 2
    27  ->     z = x + y
    28         print(z)
    29         print('Exiting...')
    '''
    ...

# Continues execution until next breakpoint or end of program
def continueCommand():
    '''
    (Pdb) continue
    (Pdb) c  # alias
    '''
    ...

# Quit debugging and exit
def quit():
    '''
    (Pdb) quit
    (Pdb) q  # alias
    '''
    ...

def main():
    set_trace()
    breakpointCommand()
    where()
    next()
    step()
    breakpoints()
    longlist()
    continueCommand()
    quit()

if __name__ == '__main__':
    main()
    print('Tests passed!')
