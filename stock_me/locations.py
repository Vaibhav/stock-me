#!/usr/bin/env python
import os


stockfile = os.path.join(os.path.expanduser('~'), 'stockme', 'stocks')


def get_stockfile():
    return stockfile
