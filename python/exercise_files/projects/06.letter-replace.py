letter = """
Dear <|NAME|>,
greetings from ABC coding house. I am happy to tell you about your selection.
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
"""
name = input("Enter your name: ")
date = input("Enter the date: ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)