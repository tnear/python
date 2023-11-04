# pprint - Data pretty printer
# https://docs.python.org/3/library/pprint.html

import pprint
import json

def jsonExample():
    data = {
        'name': 'John',
        'age': 50,
        'city': 'New York'
    }

    # convert to json string
    jsonStr = json.dumps(data, indent=4)

    print(jsonStr)
    pprint.pprint(jsonStr)

def main():
    jsonExample();

if __name__ == '__main__':
    main()
    print('Tests passed!')
