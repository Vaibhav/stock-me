StockMe
=======

[![Code Quality](https://img.shields.io/codacy/918d07d7011742e6b4bab7725c5c768b.svg)](https://www.codacy.com/app/KevinJames/stock-me)
[![Build Status](https://img.shields.io/circleci/project/TheKevJames/stock-me.svg)](https://circleci.com/gh/TheKevJames/stock-me)
[![Requirements](https://img.shields.io/requires/github/TheKevJames/stock-me.svg)](https://requires.io/github/TheKevJames/stock-me/requirements)

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
