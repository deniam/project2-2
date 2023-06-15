import pytest
from lib.grammar_stats import *

"""
Given a valid sentence with a capital letter and a full stop
Return True
"""
def test_with_valid_sentence():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Hello, this is a fine day.") == True

"""
Given a valid sentence with a capital letter but no full stop
Return True
"""
def test_with_capital_letter_but_no_ending_mark():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Hello, this is a fine day") == False

"""
"Given a sentence with no capital letter and a full stop or other mark
Returns False
"""
def test_with_lowercase_start_latter_and_full_stop():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("hello, this is a fine day.") == False

"""
"Given an empty string
Raises an error
"""
def test_with_empty_string():
    with pytest.raises(Exception) as e:
        grammar_stats = GrammarStats()
        grammar_stats.check("")
    assert str(e.value) == "This string is empty."
#Raises "Cannot check grammar of empty string"

"""
Given a valid string to percentage_good method one time
return an integer 100
"""

def test_valid_string_with_one_check():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello.")
    assert grammar_stats.percentage_good() == 100

"""
Given a valid string and then an invalid string
percentage_good method will return 50
"""

def test_valid_string_then_invalid_string_percent_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello.")
    grammar_stats.check("hello.")
    assert grammar_stats.percentage_good() == 50