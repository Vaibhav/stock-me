#!/usr/bin/env python
import ystockquote


def run(stocks):
    for stock in stocks:
        print stock + ':', ystockquote.get_price(stock)
