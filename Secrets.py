# secrets — Generate secure random numbers for managing secrets
# https://docs.python.org/3/library/secrets.html

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

def token_hex():
    # create 8 random hex characters.
    # divide by 2 because each byte of input creates 2 hex chars
    out = secrets.token_hex(nbytes = 8//2)

    print(f'{out=}')  # ex: out='76cee20c'
    assert len(out) == 8

def main():
    randint()
    choices()
    randbits()
    token_hex()

if __name__ == '__main__':
    main()
    print('Tests passed!')
