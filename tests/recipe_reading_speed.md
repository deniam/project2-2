{{PROBLEM}} Reading speed Design Recipe

1. Describe the Problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature

def estimated_reading_time(text):

    Parameters: 
    text: a representing human readable text

    Returns: 
    a float representing a reading time

    Side effects: 
    Given a text of 200 words
    It will return a reading time of 1
    Eastimate reading time ("...200...")
    => 1.0

    Given a text of 400 words
    It will return a reading time of 2
    Estimate reading time ("...400...")
    => 2.0

    Given a text of 300 words
    It will return a reading time of 1.5
    Estimate reading time ("...300...")
    => 1.5

    Given an empty string
    It will raise an error
    Estimate reading time ("")
    => Raises error: "Can't estimate reading time for empty text."


3. Create Examples as Tests

