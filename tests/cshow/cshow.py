#!/usr/bin/env python

import csv
sniffer = csv.Sniffer()

def get_delimiter(string):
    stripped_string = string.replace(" ", "")
    dialect = sniffer.sniff(stripped_string)
    return dialect.delimiter 
