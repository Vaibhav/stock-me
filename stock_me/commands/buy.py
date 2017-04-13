#!/usr/bin/env python
import ystockquote

from ..locations import get_stockfile


def run(stocks):
    with open(get_stockfile(), 'a') as data:
        for stock in stocks:
            current = ystockquote.get_price(stock)
            if isinstance(current, float):
                data.write(stock + ' ' + current + '\n')
            print 'Purchased', stock, 'at', current
