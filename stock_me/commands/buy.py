#!/usr/bin/env python
import ystockquote

from ..locations import get_dotfile


def run(stocks):
    with open(get_dotfile(), 'a') as data:
        for stock in stocks:
            current = ystockquote.get_price(stock)
            data.write(stock + ' ' + current + '\n')
            print 'Purchased', stock, 'at', current
