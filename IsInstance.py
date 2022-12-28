def fcn():
    assert isinstance(1.0, float)

def multipleTypes():
    # Use '|' to OR types together
    assert isinstance(123, int | str)
    assert isinstance('123', int | str)
    assert isinstance('abc', int | str)
    assert not isinstance(123.0, int | str)

def main():
    fcn()
    multipleTypes()

if __name__ == '__main__':
    main()
    print('Tests passed!')
