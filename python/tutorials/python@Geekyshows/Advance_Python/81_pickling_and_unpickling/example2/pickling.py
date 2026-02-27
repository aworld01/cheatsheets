import pickle
from stu import Student

n = int(input("Enter number of students: "))

with open("student.dat", mode="wb") as wf:
    for st in range(n):
        name = input("Enter student name: ")
        roll = int(input("Enter Roll: "))
        addr = input("Enter Address: ")
        stu = Student(name, roll, addr)
        pickle.dump(stu, wf)

    print("Pickling Done...")