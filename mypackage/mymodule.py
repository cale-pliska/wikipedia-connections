#!/usr/bin/env python3

# Exported function
def as_int(a):
    return int(a)

# Test function for module


def _test():
    print('hellllo')
    assert as_int('1') == 1


if __name__ == '__main__':
    _test()
