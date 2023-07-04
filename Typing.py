# typing — Support for type hints

import typing

# This function accepts an integer argument and returns a boolean
# Other primitive types include: int, float, bool, str, bytes
# Compound types include: list[int], set[str], 
def arg(value: int) -> bool:
    return value >= 0

def main():
    assert arg(1)
    assert not arg(-1)

def containers():
    # list
    a: list[int] = [1]
    
    # dictionary
    b: dict[str, float] = {'field': 2.0}

    # tuple of variable size
    t: tuple[int, ...] = (1, 2, 3)

    # list without specialized type
    l: list = [2, '3']

    assert a == [1]
    assert b == {'field': 2.0}
    assert t == (1, 2, 3)
    assert l == [2, '3']
    
# this function returns nothing (-> None)
def none() -> None:
    assert True

# Type alias creates a synonym for a type
def typeAlias():
    Vector = list[float] # type alias

    v: Vector = [1.1, 2.2, 3.3]
    assert v == [1.1, 2.2, 3.3]

# 'Any' permits any data type
def any(arg: typing.Any):
    print(arg) # print anything

if __name__ == '__main__':
    main()
    containers()
    none()
    typeAlias()
    any(1)
    any('a')

    print('Tests passed!')
