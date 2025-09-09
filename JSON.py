# json — JSON encoder and decoder
# https://docs.python.org/3/library/json.html

import json
import os

def dumps():
    # convert dictionary to JSON string
    j = {'name': 'python',
         'age': 100}

    d = json.dumps(j)
    assert d == '{"name": "python", "age": 100}'

def loads():
    jsonVar = '''
    {
        "country": {
            "name": "USA",
            "statesVisited": [
                {
                    "states": ["Missouri", "Massachusetts", "Illinois"]
                }
            ]
        }
    }
    '''
    var = json.loads(jsonVar)
    assert var['country']['name'] == 'USA'
    assert var['country']['statesVisited'][0]['states'] == ['Missouri', 'Massachusetts', 'Illinois']

def dumpLoad():
    var = {'key': 'value', '3': 'four'}
    x = json.dumps(var)
    y = json.loads(x)
    assert var == y

# load json file
def load():
    file = 'a.txt'
    with open(file, 'w', encoding='utf=8') as f:
        f.write('{"hello": 123}')

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    assert data == {'hello': 123}

    # write invalid json
    with open(file, 'w', encoding='utf-8') as f:
        f.write('hello world')

    caught_error = False
    try:
        # reading invalid json files throw exception
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        caught_error = True

    assert caught_error
    os.remove(file)

def main():
    dumps()
    loads()
    dumpLoad()
    load()

if __name__ == '__main__':
    main()
    print('Tests passed!')
