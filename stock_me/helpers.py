#!/usr/bin/env python
def print_money(money):
    if money < 0:
        print '-$' + str(abs(money))
    else:
        print '$' + str(money)
