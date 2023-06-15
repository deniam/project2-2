"""
Name of the function: count words
Argument: string
Returns: number of the words
Build-in functions to use: len()
Methods to use: .split()
"""
from lib.count_words import *

def test_words_in_the_string():
    result = count_words("It will be sunny day tomorrow and rain on day after tomorrow.")
    assert result == 12

def test_words_if_string_is_empty():
    result = count_words("")
    assert result == 0

def test_words_if_numbers_in_string():
    result = count_words("1234567890")
    assert result == 1