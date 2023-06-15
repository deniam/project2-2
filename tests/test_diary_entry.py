from lib.diary_entry import *

"""
Returns:
Given a title and contents
Format returnes a formatted entry like:
"My Title: These are the contents"
"""
def test_format_with_title_and_contents():
    diary_entry = DiaryEntry("Title", "Some contents")
    result = diary_entry.format()
    assert result == "Title: Some contents"

"""
Count words.
Returns:
int: the number of words in the diary entry
"""
def test_count_words_in_diary_entry():
    diary_entry = DiaryEntry("Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 2

"""
Parameters:
wpm: an integer representing the number of words the user can read 
per minute
Returns:
int: an estimate of the reading time in minutes for the contents at
the given wpm.
"""
def test_reading_time():
    diary_entry = DiaryEntry("Title", "Some contents")
    result = diary_entry.reading_time(1)
    assert result == 2

"""

# Parameters
wpm: an integer representing the number of words the user can read
per minute
minutes: an integer representing the number of minutes the user has
to read
Returns:
string: a chunk of the contents that the user could read in the
given number of minutes

If called again, `reading_chunk` should return the next chunk,
skipping what has already been read, until the contents is fully read.
The next call after that should restart from the beginning.
"""

def test_reading_chunk():
    diary_entry = DiaryEntry("Title", "Some contents is exists")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "Some contents is exists"

def test_reading_chunk_called_again():
    diary_entry = DiaryEntry("Title", "Some contents is exists one two three four")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"