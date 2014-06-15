import argparse

from .commands import (buy, check, sell, suggest)


__version__ = 'alpha'


def get_params():
    parser = argparse.ArgumentParser(description='Evaluate stock trends.',
        usage='stock-me [-h] [-v] <command> <stocks>', add_help=False)
    required = parser.add_argument_group('required arguments')
    required.add_argument('command', nargs=1, help='Command to apply')
    optional = parser.add_argument_group('options')
    optional.add_argument('stocks', nargs='*',
        help='''Name of stock(s) to run<command> against
             (if command calls for stocks)''')
    system = parser.add_argument_group('information')
    system.add_argument('-h', '--help', action='help')
    system.add_argument('-v', '--version', action='version',
        version='StockMe ' + __version__)
    args = parser.parse_args()

    return args.command, args.stocks


def execute_from_command_line():
    command, stocks = get_params()

    if command[0] in {'check'}:
        check.run(stocks)
    elif command[0] in {'buy'}:
        buy.run(stocks)
    elif command[0] in {'sell'}:
        sell.run(stocks)
    elif command[0] in {'suggest'}:
        suggest.run()
