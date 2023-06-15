{{PROBLEM}} Improve Grammar Design Recipe

1. Describe the Problem
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

We'll ignore any interediate sentences.

2. Design the Function Signature

```python
def check_sentence_grammar(text):
    #Parameters:
    #   text: a starting representing human-readable text
    #Returns:
    #   boolean, true if valid, false othersvise


3. Create Examples as Tests

```python

# """
# Given a valid sentence with a capital letter and a full stop
# Return True
# """
# check_sentence_grammar("Hello, this is a fine day.")
# # => True

# """
# Given a valid sentence with a capital letter and a question mark
# Return True
# """
# check_sentence_grammar("Hello, this is a fine day?")
# # => True

# """
# Given a sentence with a capital letter and a exclamation mark
# Returns False
# """
# check_sentence_grammar("Hello, this is a fine day!")
# # => True

# """
# Given a sentence with a capital letter but no full stop or other mark
# Returns False
# """
# check_sentence_grammar("Hello, this is a fine day")
# # => False

# """
# Given a sentence with a capital letter but ends with a comma
# Returns False
# """
# check_sentence_grammar("Hello, this is a fine day")
# # => False

# """
# Given a sentence with a capital letter but ends with a colon
# Returns False
# """
# check_sentence_grammar("Hello, this is a fine day:")
# # => False

# """
# "Given a sentence with no capital letter and a full stop or other mark
# Returns False
# """
# check_sentence_grammar("hello, this is a fine day.")
# # => False
 
# """
# "Given an empty string
# Raises an error
# """
# check_sentence_grammar("")
# #Raises "Cannot check grammar of empty string"

