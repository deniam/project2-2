import pytest
from lib.improve_grammar import *

"""
Given a valid sentence with a capital letter and a full stop
Return True
"""
def test_with_valid_sentence():
    result = check_sentence_grammar("Hello, this is a fine day.")
    assert result == True

"""
Given a valid sentence with a capital letter but no full stop
Return True
"""
def test_with_capital_letter_but_no_ending_mark():
    result = check_sentence_grammar("Hello, this is a fine day")
    assert result == False

"""
Given a valid sentence with a capital letter and a question mark
Return True
"""
def test_with_capital_letter_and_question_mark():
    result = check_sentence_grammar("Hello, this is a fine day?")
    assert result == True

"""
Given a sentence with a capital letter and a exclamation mark
Returns False
"""
check_sentence_grammar("Hello, this is a fine day!")
# => True

"""
Given a sentence with a capital letter and a exclamation mark
Returns False
"""
def test_with_capital_letter_and_exclamation_mark():
    result = check_sentence_grammar("Hello, this is a fine day!")
    assert result == True

"""
Given a sentence with a capital letter but ends with a comma
Returns False
"""
def test_with_capital_letter_and_comma():
    result = check_sentence_grammar("Hello, this is a fine day")
    assert result == False

"""
Given a sentence with a capital letter but ends with a colon
Returns False
"""
def test_with_capital_letter_and_colon():
    result = check_sentence_grammar("Hello, this is a fine day:")
    assert result == False

"""
"Given a sentence with no capital letter and a full stop or other mark
Returns False
"""
def test_with_lowercase_start_latter_and_full_stop():
    result = check_sentence_grammar("hello, this is a fine day.")
    assert result == False

    """
"Given an empty string
Raises an error
"""
def test_with_empty_string():
    with pytest.raises(Exception) as e:
        check_sentence_grammar("")
    error_message = str(e.value)
    assert error_message == "This string is empty."
#Raises "Cannot check grammar of empty string"
