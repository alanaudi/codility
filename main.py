#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Standard import

# Third-party import
import click
from tabulate import tabulate

# Local import

class EasyDict(dict): # {{{
    def __init__(self, *args, **kwargs):
        super(EasyDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
# }}}
# Golbal Settings {{{
_global_test_options = [
        # click.option('-test', '--test-arg', 'var_name', default='default value', help='Please customize option value'),
        click.option('-n', 'n', default=28, help='28'),
        click.option('-l', 'l', default=[1, 12, 19, 7, 5, 11, 13, 16, 18, 10,  2,  6, 17, 14,  4,  3, 15,  8,  0,  9], help='list'),
        ]
def global_test_options(func):
    for option in reversed(_global_test_options):
        func = option(func)
    return func
# }}}

@click.group()
@global_test_options
def main(**kwargs): # {{{
    pass
# }}}

@main.command()
@global_test_options
def test_a(**kwargs):
    def return_sum(x): # {{{
        _sum = 0
        while int(x) > 0:
            x = int(x)
            d = x % 10
            x /= 10
            _sum += d
        return _sum
    # }}}
    # Print argument, option, parameter {{{
    print(tabulate(list(kwargs.items()), headers=['Name', 'Value'], tablefmt='orgtbl'))
    args = EasyDict(kwargs)
    n = args.n
    # }}}
    MAX = 50000
    assert n >= 1 and n <= MAX
    sum_of_digit = return_sum(n)
    for i in range(n+1, 10*MAX + 1):
        if return_sum(i) == sum_of_digit:
            print(F"N = {i}")
            break

@main.command()
@global_test_options
def test_b(**kwargs):
    # Print argument, option, parameter {{{
    print(tabulate(list(kwargs.items()), headers=['Name', 'Value'], tablefmt='orgtbl'))
    args = EasyDict(kwargs)
    n = args.n
    # }}}
    MIN_LENGTH = 0
    MAX_LENGTH = 1000000
    l = args.l
    assert len(l) >= MIN_LENGTH and n <= MAX_LENGTH

    neckless = ['s']
    create_new = True

    # mapping = {index:item for index, item in enumerate(l)}
    mapping = [(bead, next_bead) for bead, next_bead in enumerate(l)]
    head = None
    while len(mapping) > 0:
        for item in mapping:
            if head == None: head = item[0]
            if neckless[-1] == 's':
                neckless.extend([item[0], item[1]])
                mapping.remove(item)
                head = item[0]
                continue
            if neckless[-1] != item[0]: continue
            if head == item[1]:
                neckless.extend(['s'])
                head = None
                mapping.remove(item)
                continue
            if neckless[-1] == item[0]:
                neckless.append(item[1])
                mapping.remove(item)
                continue
            if item[0] == item[1]:
                neckless.extend([item[0], 's'])
                head = None
                mapping.remove(item)
                continue
    idx_list = [idx for idx, val in enumerate(neckless) if val == 's']
    res = [neckless[i: j] for i, j in zip([0] + idx_list, idx_list + ([len(neckless)] if idx_list[-1] != len(neckless) else []))]
    print(res)
    print(max([len(l) for l in res]) - 1)
if "__main__" == __name__:
    main()
