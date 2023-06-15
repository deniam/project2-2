import pytest
from lib.reading_speed import reading_speed

"""
Given a text of 200 words
It will return a reading time of 1
"""
def test_with_two_hundred_words():
    text = " ".join(['word' for i in range (0, 200)])
    result = reading_speed(text)
    assert result == 1.0

def test_with_four_hundred_words():
    text = " ".join(['word' for i in range(0, 400)])
    result = reading_speed(text)
    assert result == 2.0

def test_with_three_hundred_words():
    text = " ".join(['word' for i in range(0, 300)])
    result = reading_speed(text)
    assert result == 1.5

def test_with_empty_string():
    with pytest.raises(Exception) as e:
        reading_speed("")
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time for an empty text."