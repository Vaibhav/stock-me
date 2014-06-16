#!/usr/bin/env python
from ..locations import get_stockfile
from .ticker import run as ticker


def run():
    owned = []
    for line in open(get_stockfile(), 'r').readlines():
        owned.append(line.split()[0])

    try:
        ticker(owned)
    except KeyboardInterrupt:
        return
