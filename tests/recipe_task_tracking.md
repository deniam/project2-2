{{PROBLEM}} Tracking of the tasks Design Recipe

1. Describe the Problem
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature

```python
def check_if_the_string_includes(text):
    #Parameters:
    #   text: text should include the string #TODO
    #Returns:
    #   boolean, true if valid, false othersvise


3. Create Examples as Tests

```python

# """
# Given a valid text with a string "#TODO"
# Returns True
# """
# check_task_tracking("""
# #TODO
# shopping;
# gym;
# work;
# book tickets.
# """)
# # => True

# """
# Given a text without a string "#TODO"
# Returns False
# """
# check_task_tracking("""
# shopping;
# gym;
# work;
# book tickets.
# """)
# # => False

# """
# Given an empty string
# Raises Error message
# """
# check_task_tracking("")
# # => Raise error_message "Text doesn't include #TODO string"