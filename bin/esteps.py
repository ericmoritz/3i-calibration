"""
Usage:
    esteps.py <esteps> <wanted> <start> <end>
"""
from docopt import docopt
from decimal import Decimal as D

def calc(esteps, wanted, start, end):
    extruded = (start - end)
    return round(wanted / extruded * esteps)

def test(expected, got):
    assert expected == got, "Expected {expected} got {got}".format(**locals())

# Make sure the function works
test(D(928), calc(D(900), D(100), D(120), D(23)))

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    esteps = arguments['<esteps>']
    wanted = arguments['<wanted>']
    start = arguments['<start>']
    end = arguments['<end>']
    print calc(
        D(esteps),
        D(wanted),
        D(start),
        D(end)
    )
