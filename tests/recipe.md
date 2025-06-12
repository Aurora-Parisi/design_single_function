## 1. Describe the Problem 

_Put or write the user story here. Add any clarifying notes you might have._

"""
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.
"""


## 2. Design the function signature

_Include the name of the function, its parameters, return value, and side effects._

def includes_todo(text)

Parameters: string representing a line from user's notes

Returns: 
True if the string contains "#TODO"

Side effects:
None

## 3. Create Examples of Tests

_Make a list of examples of what the function will take and return._

_Encode each example as a test. You can add to the above list as you go._


Example 1: 

Test if string does NOT contain #TODO
returns false

Example 2:

Test if string contains #TODO
returns True


Example 3:

Test if string contains #todo or #Todo
returns True

Example 4:

Test if string is empty
return False


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!

