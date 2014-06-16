#!/usr/bin/env python
import ystockquote

from ..locations import get_dotfile


def run(stocks):
    overall = 0
    owned = []
    for line in open(get_dotfile(), 'r').readlines():
        if any(line.startswith(stock) for stock in stocks):
            purchased = line.split()
            current = ystockquote.get_price(purchased[0])
            profit = (float(current) - float(purchased[1]))
            overall += profit
            print 'Sold', purchased[0], 'at', current + '.',
            print 'Return was',
            if profit < 0:
                print '-$' + str(abs(profit))
            else:
                print '$' + str(profit)
        else:
            owned.append(line)

    with open(get_dotfile(), 'w') as data:
        for stock in owned:
            data.write(stock)

    print 'Overall return:',
    if overall < 0:
        print '-$' + str(abs(overall))
    else:
        print '$' + str(overall)
