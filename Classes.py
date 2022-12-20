# properties:
class MyProp:
    prop = 5

    def setProp(self, value):
        self.prop = value

    def getProp(self):
        return self.prop

class Person:
    def __init__(self, name):
        self.name = name

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

def properties():
    m = MyProp()
    assert m.prop == 5

    m.setProp(6)
    assert m.getProp() == 6

def constructor():
    p = Person('person')
    assert p.name == 'person'

def iterator():
    it = IteratorClass()
    values = []
    for x in iter(it):
        values.append(x)

    assert values == [1, 2, 3]

def main():
    properties()
    constructor()
    iterator()

if __name__ == '__main__':
    main()
    print('Tests passed!')
