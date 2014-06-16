import os

import ystockquote


datafile = os.path.join(os.path.expanduser('~'), '.stockme')


def run(stocks):
    with open(datafile, 'a') as data:
        for stock in stocks:
            current_price = ystockquote.get_price(stock)
            data.write(stock + ' ' + current_price + '\n')
            print 'Purchased', stock, 'at', current_price
