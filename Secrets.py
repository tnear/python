import secrets

def randint():
    csprng = secrets.SystemRandom()
    randNum = csprng.randint(1, 10)
    assert randNum <= 10

def choices():
    csprng = secrets.SystemRandom()
    numList = [5, -3, 14, 2]
    secureChoice = csprng.choice(numList)
    assert secureChoice in numList

def randbits():
    # generate 256 random bits
    randBits = secrets.randbits(256)
    print(randBits)

def main():
    randint()
    choices()
    randbits()

if __name__ == '__main__':
    main()
    print('Tests passed!')
