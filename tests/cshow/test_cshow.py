import pytest
import sys
import cshow as sut

def test_get_delimiter_finds_commas_with_no_spaces():
    string = "first,second,third,fourth"
    assert sut.get_delimiter(string) == ','


def test_get_delimiter_finds_pipes_with_no_spaces():
    string = "first|second|third|fourth"
    assert sut.get_delimiter(string) == '|'


def test_get_delimiter_finds_commas_with_spaces():
    string = "first ,second ,third ,fourth"
    assert sut.get_delimiter(string) == ','


def test_get_delimiter_finds_pipes_with_spaces():
    string = "first |second |third |fourth"
    assert sut.get_delimiter(string) == '|'
