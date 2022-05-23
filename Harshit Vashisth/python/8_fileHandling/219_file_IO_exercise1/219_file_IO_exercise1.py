"""
#salary.txt
Harshit, 100
Mohit, 50
Aaditya, 200
Nitish, 500


#output.txt
Harshit's salary is 100
Mohit's salary is 50
Aaditya's salary is 200
Nitish's salary is 500
"""
with open("salary.txt") as rf:
    with open("output.txt", "a") as wf:
        for line in rf.readlines():
            name, salary = line.split(",")
            wf.write(f"{name}'s salary is {salary}")