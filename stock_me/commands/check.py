#!/usr/bin/env python
from __future__ import division

import ystockquote

from ..locations import get_stockfile


def run():
    for line in open(get_stockfile(), 'r').readlines():
        purchased = line.split()
        current = ystockquote.get_price(purchased[0])
        difference = 100 * round(float(current) / float(purchased[1]) - 1, 5)

        print purchased[0] + ':',
        print 'bought at', purchased[1] + ',',
        print 'current price is', current,
        print '(' + str(difference) + '%)'
