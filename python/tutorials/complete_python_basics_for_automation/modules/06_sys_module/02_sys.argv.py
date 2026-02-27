"""
sys.argv returns a list of command line arguments in string and passed to a python script.
example:
    python 12_sys.argv.py hi how are you 124 ("hi how are you 124" commandLine arguments)
"""

import sys

value = sys.argv
print(value[1:])