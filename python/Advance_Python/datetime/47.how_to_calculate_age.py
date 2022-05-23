from datetime import date
dob = date(1989, 2, 10)
today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

print(age)
