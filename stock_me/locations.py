#!/usr/bin/env python
import os


stockme_dir = os.path.join(os.path.expanduser('~'), '.stockme')
stockfile = os.path.join(stockme_dir, 'stocks')

if not os.path.isfile(stockfile):
    if not os.path.exists(stockme_dir):
        os.mkdir(stockme_dir)
    open(stockfile, 'w').close()


def get_stockfile():
    return stockfile
