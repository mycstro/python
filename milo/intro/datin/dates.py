# -*- coding: utf-8 -*-
import sys


def format_dbirth(bdat):
    """
    Format birthdate. [MM/DD/YYYY]
    """
    ainfo = bdat
    month, day, year = map(int, ainfo.split('/'))
    # print(month, day, year)
    return month, day, year