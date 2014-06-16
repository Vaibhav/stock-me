#!/usr/bin/env python
import os


dotfile = os.path.join(os.path.expanduser('~'), '.stockme')


def get_dotfile():
    return dotfile
