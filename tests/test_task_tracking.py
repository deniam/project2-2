import pytest

from lib.task_tracking import *

"""
Given a valid text with a string "#TODO"
Returns True
"""
def test_if_text_contains_todo():
    tasklist = check_task_tracking("""
    #TODO
    shopping;
    gym;
    work;
    book tickets.
    """)
    assert tasklist == True

"""
Given a text without a string "#TODO"
Returns False
"""
def test_if_text_not_contains_todo():
    tasklist = check_task_tracking("""
    shopping;
    gym;
    work;
    book tickets.
    """)
    assert tasklist == False

"""
Given an empty string
Raises Error message
"""
def test_if_text_is_empty():
    with pytest.raises(Exception) as e:
        check_task_tracking("")
    error_message = str(e.value)
    assert error_message == "Text doesn't include #TODO string"