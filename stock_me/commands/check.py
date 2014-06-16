from __future__ import division

import os

import ystockquote


datafile = os.path.join(os.path.expanduser('~'), '.stockme')


def run():
    for line in open(datafile, 'r').readlines():
        purchased = line.split()
        current = ystockquote.get_price(purchased[0])
        difference = 100 * round(float(current) / float(purchased[1]) - 1, 5)
        print purchased[0] + ':',
        print 'bought at', purchased[1] + ',',
        print 'current price is', current,
        print '(' + str(difference) + '%)'
