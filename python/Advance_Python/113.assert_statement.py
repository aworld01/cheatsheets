'''
The assert_statement is useful to ensure that a given condition is True. If it's not true, it raises AssertionError.
Syntax:- assert condition, error_message

If the condition is False then the exception by the name AssertionError is raised along with the message.

If message is not given and the condition is False then also AssertionError is raised without message.
'''

## AssertionError without message.
# a = 20
# assert a<=10

## AssertionError with message.
a = 20
assert a<=10, 'Invalid Number'