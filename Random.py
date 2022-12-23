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

def main():
    rand()
    randrange()
    choice()

if __name__ == '__main__':
    main()
    print('Tests passed!')
