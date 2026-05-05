# Notes on Python classes.

import typing

# Properties:
class MyProp:
    # static variables shared by all instances
    prop = 5
    _radius = 10

    def setProp(self, value):
        self.prop = value
        self._radius = 10

    def getProp(self):
        return self.prop

    # classes use the @staticmethod decorator
    #   ex: assert MyProp.staticMethod() == 101
    @staticmethod
    def staticMethod():
        return 101

    # the property decorator allows you to access a property
    # using classInstance.prop (no parentheses) but it invokes a function
    @property
    def radius(self):
        print('Getting radius...')
        return self._radius

class Person:
    def __init__(self, name):
        self.name = name

class IteratorClass:
    def __init__(self):
        self.a = 1

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

def staticMethod():
    value = MyProp.staticMethod()
    assert value == 101

def methodDecorator():
    mp = MyProp()
    assert mp.radius == 10

def static_variables():
    assert MyProp.prop == 5
    MyProp.prop = 6
    assert MyProp.prop == 6

# Forward references are type annotations that refer to a type
# that has not been fully defined yet. It is most common for
# self-referential classes, such as linked list because Python
# is still in the middle of creating the class.
class Node:
    # forward references put type in quotes: "Node" instead of Node
    def __init__(self, next: "Node"):
        self.next = next

def forward_reference():
    # this test will fail if "Node" (above) is not in quotes
    hints = typing.get_type_hints(Node.__init__)
    assert 'next' in hints

def main():
    properties()
    constructor()
    iterator()
    staticMethod()
    methodDecorator()
    static_variables()
    forward_reference()

if __name__ == '__main__':
    main()
    print('Tests passed!')
