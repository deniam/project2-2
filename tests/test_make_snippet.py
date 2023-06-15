"""
Argument = string
Objectives:
first 5 words
or
first 5 words + "..." if it's more than 5

Process:
Make a function
Calculate number of words
Use ifelse method to get objectives
Use len and split methods
"""
from lib.make_snippet import *

# def test_how_long_string_is():
#     result = make_snippet("Today I'm going to supermarket")
#     assert result == 5

def test_if_number_of_words_five_or_less():
    result = make_snippet("Today I'm going to supermarket")
    assert result == "Today I'm going to supermarket"

def test_if_number_of_words_more_than_five():
    result = make_snippet("Today I want to book a tickets somewhere")
    assert result == "Today I want to book a tickets somewhere..."