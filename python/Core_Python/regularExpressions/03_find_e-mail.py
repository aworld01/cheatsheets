'''
\d: Any numeric digit from 0 to 9.
\D: Any character that is not a numeric digit from 0 to 9.
\w: Any letter, numeric digit, or the underscore character. (Think of this as matching "word" character.)
\w+: to take the whole word.
\W: Any character that is not a letter, numeric digit, or the underscore character.
\s: Any Space, Tab, or newline character. (Think of this as matching "space" characters.)
\S: Any character that is not a Space, Tab, or newline.
'''

import re
s="Hello this string gf g dfg df dfg abdulzoha786@gmail.com +919006228083"
def getEmails(s):
    eRegex=re.compile(r'\D\w+@\w+.\w+')
    em=eRegex.findall(s)
    if em:
        return em
    else:
        return None

print(getEmails(s))
