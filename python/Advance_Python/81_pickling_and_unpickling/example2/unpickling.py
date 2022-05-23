import pickle
from stu import Student
with open("student.dat", mode="rb") as rf:
    while True:
        try:
            obj = pickle.load(rf)
            obj.disp()
        except EOFError:
            print("Unpickling Done...")
            break