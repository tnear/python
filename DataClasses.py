'''
dataclasses provide decorators and functions to generate special methods,
such as __init__ and __repr__, automatically.
https://docs.python.org/3/library/dataclasses.html
'''

import dataclasses

@dataclasses.dataclass
class Person:
    # no need to create __init__ constructor.
    # @dataclass avoids need to duplicate every property name.
    # every property needs its type specified.
    first_name: str
    last_name: str
    age: int
    # default values must be listed last, same as with function arguments
    country: str = 'United States'

    # use __post_init__ to verify initialization instead of __init__
    def __post_init__(self):
        assert len(self.first_name) > 0
        assert len(self.last_name) > 0
        assert self.age >= 0
        assert len(self.country) > 0

    def full_name(self) -> str:
        return self.first_name + ' ' + self.last_name

def test_person():
    p = Person('First', 'Last', 50)
    assert p.first_name == 'First'
    assert p.last_name == 'Last'
    assert p.age == 50
    assert p.country == 'United States'
    assert p.full_name() == 'First Last'

def main():
    test_person()

if __name__ == '__main__':
    main()
    print('Tests passed!')
