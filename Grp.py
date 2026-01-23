'''
grp - The group database
https://docs.python.org/3/library/grp.html
'''

import grp

def group_all():
    # get all groups
    group_info = grp.getgrall()
    assert len(group_info) > 0
    assert isinstance(group_info[0], grp.struct_group)

def main():
    group_all()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
