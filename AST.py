'''
ast — Abstract Syntax Trees
https://docs.python.org/3/library/ast.html
'''

import ast

# literal_eval() parses strings into python data structures
def literal_eval():
    # convert dictionary string into actual dictionary
    dict_string = "{'name': 'John', 'age': 50}"
    d = ast.literal_eval(dict_string)

    assert isinstance(d, dict)
    assert d == {
        'name': 'John',
        'age': 50
    }

def main():
    literal_eval()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
