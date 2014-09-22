StockMe
=======

[![Build Status](https://travis-ci.org/TheKevJames/stock-me.svg?branch=master)](https://travis-ci.org/TheKevJames/stock-me.git)
[![Coverage Status](https://coveralls.io/repos/TheKevJames/stock-me/badge.png?branch=master)](https://coveralls.io/r/TheKevJames/stock-me?branch=master)
[![Dependency Status](https://gemnasium.com/TheKevJames/stock-me.svg)](https://gemnasium.com/TheKevJames/stock-me)


StockMe is a simple command-line utility for evaluating stock trends.

Installation
============

You can build StockMe from source by cloning this repo and running:

    python setup.py install

Usage
=====

StockMe supports the following commands:
* `stock-me check` == check the current vs purchase price of each stock you own
* `stock-me lookup <stocks>` == look up the current price of a list of stocks
* `stock-me buy <stocks>` == purchase one of each listed stock at current market price
* `stock-me sell <stocks>` == sell all of each listed stock at current market price, display your profits or losses
* `stock-me ticker <stocks>` == generate a ticker for each listed stock
* `stock-me watch` == generate a ticker for each stock you own

And coming soon:
* `stock-me suggest` == evalute trends to suggest purchases or sales
