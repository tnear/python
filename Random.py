import random

def rand():
    # random generates a float between 0 and 1
    r = random.random()
    assert r >= 0
    assert r < 1

def randrange():
    # [start, stop)
    # Generate random number between [0, 10]
    r = random.randrange(1, 11)
    assert r >= 0
    assert r <= 10

def choice():
    # choose random element
    s = 'string'
    c = random.choice(s)
    assert c in s

def uniform():
    # Generate random number between [a, b] (inclusive)
    # Between 0, 10
    r = random.uniform(0, 10)
    assert r >= 0 and r <= 10

    # Between 20, 80
    r = random.uniform(20, 80)
    assert r >= 20 and r <= 80

def main():
    rand()
    randrange()
    choice()
    uniform()

if __name__ == '__main__':
    main()
    print('Tests passed!')
