import os

import ystockquote


datafile = os.path.join(os.path.expanduser('~'), '.stockme')


def run(stocks):
    profit = 0
    owned = []
    for line in open(datafile, 'r').readlines():
        if any(line.startswith(stock) for stock in stocks):
            purchased = line.split()
            profit += (float(ystockquote.get_price(purchased[0]))
                       - float(purchased[1]))
        else:
            owned.append(line)

    with open(datafile, 'w') as data:
        for stock in owned:
            data.write(stock)

    print 'Profit:',
    if profit < 0:
        print '-$' + str(abs(profit))
    else:
        print '$' + str(profit)
