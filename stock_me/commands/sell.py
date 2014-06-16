#!/usr/bin/env python
import ystockquote

from ..helpers import print_money
from ..locations import get_stockfile


def run(stocks):
    overall = 0
    owned = []
    for line in open(get_stockfile(), 'r').readlines():
        if any(line.startswith(stock) for stock in stocks):
            purchased = line.split()
            current = ystockquote.get_price(purchased[0])
            profit = round(float(current) - float(purchased[1]), 3)
            overall += profit

            print 'Sold', purchased[0], 'at', current + '.',
            print 'Return was',
            print_money(profit)
        else:
            owned.append(line)

    with open(get_stockfile(), 'w') as data:
        for stock in owned:
            data.write(stock)

    print 'Overall return:',
    print_money(overall)
