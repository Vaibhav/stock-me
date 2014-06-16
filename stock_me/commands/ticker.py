#!/usr/bin/env python
import time

import ystockquote


def run(stocks):
    stocks.sort()
    for stock in stocks:
        print stock.ljust(8),
    print ''

    try:
        while True:
            tick(stocks)

            time.sleep(1)
    except KeyboardInterrupt:
        return

def tick(stocks):
    for stock in stocks:
        print ystockquote.get_price(stock).ljust(8),
    print ''
