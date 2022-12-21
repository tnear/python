import json

def dumps():
    # convert dictionary to JSON string
    j = {'name': 'python',
         'age': 100}

    d = json.dumps(j)
    assert d == '{"name": "python", "age": 100}'

def loads():
    jsonVar = """
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
    """
    var = json.loads(jsonVar)
    assert var['country']['name'] == 'USA'
    assert var['country']['statesVisited'][0]['states'] == ['Missouri', 'Massachusetts', 'Illinois']

def dumpLoad():
    var = {'key': 'value', '3': 'four'}
    x = json.dumps(var)
    y = json.loads(x)
    assert var == y

def main():
    dumps()
    loads()
    dumpLoad()

if __name__ == '__main__':
    main()
    print('Tests passed!')
