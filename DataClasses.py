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

# Use frozen=true to make instances immutable after creation
@dataclasses.dataclass(frozen=True)
class User:
    name: str
    age: int

def test_user():
    u = User('hello', 50)
    assert u.name == 'hello'
    assert u.age == 50

    # Modifying a field throws:
    # dataclasses.FrozenInstanceError: cannot assign to field 'name'
    # u.name = 'new name'

def to_dictionary():
    u = User('me', 25)
    # asdict() converts dataclass to dictionary
    d = dataclasses.asdict(u)
    assert d == {'name': 'me', 'age': 25}

# Python class bodies run once when the class is defined.
# Because mutable defaults would be shared, python disallows
# the example below
# @dataclasses.dataclass
# class MutableDefault:
#     items: list[str] = []  # not allowed: lists are mutable
#     count: int = 3         # allowed: '3' is immutable
#     value: bool = True     # allowed: True is immutable

# Python's solution to problem above is 'default_factory'. It says
# when creating a new class instance, always create a new <type>.
@dataclasses.dataclass
class MutableDeafult:
    items: list[str] = dataclasses.field(default_factory=list)

def default_factory():
    m = MutableDeafult()
    m2 = MutableDeafult()

    # Updating m's items does not impact m2. They are separate lists
    # due to their creation with default_factory.
    m.items.append("hello")
    assert m.items == ["hello"]
    assert m2.items == []

@dataclasses.dataclass
class UserInitFalse:
    name: str
    # use init=False when a field is part of the dataclass, but not
    # accepted as a parameter to generated __init__ method
    normalized_name: str = dataclasses.field(init=False)

    def __post_init__(self):
        self.normalized_name = self.name.lower()

def init_false():
    u = UserInitFalse('Alice')
    print(u)

# dataclasses.replace creates new dataclass instance by copying
# an existing one and overriding selected fields.
def replace():
    p = Person('hello', 'last', 50)

    # create new person by replacing first name
    p_replaced = dataclasses.replace(p, first_name='goodbye')
    assert p_replaced.first_name == 'goodbye'
    assert p.last_name == 'last'

    # original person is unchanged
    assert p.first_name == 'hello'

def main():
    test_person()
    test_user()
    to_dictionary()
    default_factory()
    init_false()
    replace()

if __name__ == '__main__':
    main()
    print('Tests passed!')
