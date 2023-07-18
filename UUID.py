# uuid — UUID objects
# https://docs.python.org/3/library/uuid.html

import uuid

def uuid4():
    # make random uuid, ex: UUID('4812ac9a-9fa3-4fe1-8cb2-3e3ae341882d')
    u = uuid.uuid4()
    assert isinstance(u, uuid.UUID)

    # convert to string, ex: '4812ac9a-9fa3-4fe1-8cb2-3e3ae341882d'
    uStr = str(u)
    assert isinstance(uStr, str)

    # convert to hex string, ex: '4812ac9a9fa34fe18cb23e3ae341882d'
    uHex = u.hex
    assert isinstance(uHex, str)

def main():
    uuid4()

if __name__ == '__main__':
    main()
    print('Tests passed!')
