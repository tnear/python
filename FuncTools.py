import functools

class PowerClass:
    def __init__(self):
        self.prop = 1

    def setProp(self, value):
        self.prop = value

    set10 = functools.partialmethod(setProp, value=10)
    set100 = functools.partialmethod(setProp, value=100)

def power(a, b):
    return a ** b

# Applies function repeatedly to two elements to reduce to one value
def reduce():
    val = [2, 4, 7, 9, 1, 3]
    sumOfVal = functools.reduce(lambda a, b : a + b, val)
    assert sumOfVal == 26

    sumOfVal = functools.reduce(lambda a, b : a + b, [25])
    assert sumOfVal == 25

# partial objects are callable objects created by functools.partial()
def partial():
    pow2 = functools.partial(power, b=2)
    assert pow2.func == power
    assert pow2.args == ()
    assert pow2.keywords == {'b': 2}

    # usage of pow with b=2
    assert pow2(3) == 9
    assert pow2(-5) == 25

# partialmethod are similar to partial except are not directly callable
def partialmethod():
    pow2 = functools.partialmethod(power, b=2)
    assert pow2.func == power
    assert pow2.args == ()
    assert pow2.keywords == {'b': 2}

    p = PowerClass()
    assert p.prop == 1
    p.set10()
    assert p.prop == 10
    p.set100()
    assert p.prop == 100

# Without @functools.cache, the implementation below takes exponential time
# Note: lru_cache offers fine-grained control
@functools.cache
def fibonacci(n):
    if n <= 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

def cache():
    # @functools.cache memoizes results of recursive calls
    # by caching values, fibonacci runs in linear time instead of exponential
    assert fibonacci(150) == 16130531424904581415797907386349

@functools.singledispatch
def printer(arg):
    return arg

@printer.register(int)
def _(arg):
    return arg * 2

@printer.register(float)
def _(arg):
    return arg / 2

# singledispatch can be used for overloading types
def singledispatch():
    assert printer('abc') == 'abc'
    assert printer(10) == 20
    assert printer(10.0) == 5.0

def main():
    reduce()
    partial()
    partialmethod()
    cache()
    singledispatch()

if __name__ == '__main__':
    main()
    print('Tests passed!')
