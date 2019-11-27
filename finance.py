#!/usr/bin/env python

from yahoo_fin import stock_info as si
import xlwings as xw
from os.path import expanduser, join


def get_previous_close(ticker):
    return si.get_quote_table(ticker)['Previous Close']


def write_stocks():

    home = expanduser("~")
    file_path = join(home, 'Dropbox', 'documents', 'budget.xlsb')

    wb = xw.Book(file_path)
    sht1 = wb.sheets['Investment']
    sht1.range('C3').value = str(round(get_previous_close("VTxx"), 2))
    sht1.range('C4').value = str(round(get_previous_close("VTxx"), 2))
    wb.save()
    wb.close()


if __name__ == "__main__":
    write_stocks()
