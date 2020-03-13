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
        click.option('-l', 'l', default=[5,4,0,3,1,6,2], help='28'),
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

    neckless = []
    create_new = True

    # mapping = {index:item for index, item in enumerate(l)}
    mapping = [(bead, next_bead) for bead, next_bead in enumerate(l)]

    while len(mapping) > 0:
        for item in mapping:
            print(neckless)
            print(item[0], item[1])
            if len(neckless) == 0 or neckless[-1] == 'stop':
                neckless.extend([item[0], item[1]])
                # del mapping[bead]
                mapping.pop(item)
                continue
            if neckless[-1] != item[0]: continue
            if neckless[-1] == item[0]:
                neckless.append(item[1])
                # del mapping[bead]
                mapping.pop(item)
            print(neckless)
            print(mapping)
if "__main__" == __name__:
    main()
