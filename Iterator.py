class IteratorClass:
    # __iter__ returns start state
    def __iter__(self):
        self.a = 1
        return self

    # __next__ updates state and returns old value
    def __next__(self):
        if self.a > 3:
            # StopIteration ends infinite loop
            raise StopIteration
        x = self.a
        self.a += 1
        return x

def iterator():
    it = IteratorClass()
    values = []
    for x in iter(it):
        values.append(x)

    assert values == [1, 2, 3]

def tupleIterate():
    tup = ('a', 'b', 'c')

    it = iter(tup)

    assert next(it) == 'a'
    assert next(it) == 'b'
    assert next(it) == 'c'

def dictIterate():
    d = {'a': 1,
         'b': 2,
         'c': 3}

    it = iter(d)

    assert next(it) == 'a'
    assert next(it) == 'b'
    assert next(it) == 'c'

def main():
    iterator()
    tupleIterate()
    dictIterate()

if __name__ == '__main__':
    main()
    print('Tests passed!')
