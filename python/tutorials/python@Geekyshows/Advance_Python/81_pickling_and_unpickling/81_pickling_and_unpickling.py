"""
Pickling is a process of converting a class object into a byte stream so that it can be stored into a file. This is also called as object serialization.
We use pickle module to perform pickling and unpickling.

FUNCTION
dump(): This function is used to perform the pickling. It returns the pickled representation of the object as a bytes object, instead of writing it to a file.
This method belongs to pickle module.
Syntax:-
    import pickle
    pickle.dump(object, file)


Unpickling is a process whereby byte steam is converted back into a class object. It is inverse operation of pickling. This is also called as de-serialization.
Pickling and unpickling should be done using binary files since they support byte streams.

FUNCTION
load(): This function is used to read an pickled object from a binary file and returns it into object. This method belongs to pickle module.
Syntax:-
    import pickle
    pickle.load(file)


Warning: The pcikle module is not secure against erroneous or maliciously constructed data. Never umpickle data received from an untrusted or unauthenticated source.


WHY DO WE NEED PICKLING AND UNPICKLING
When we store some structured data in the file and want to perform calculation that time we need pickling and unpickling
05:49 / 39:33
"""
import pickle

class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address
    def disp(self):
        print(f"Name: {self.name} Roll: {self.roll} Address {self.address}")

with open("student.dat", mode="wb") as wf:
    stu = Student("Rahul:", 101, "Ranchi")
    stu2 = Student("Sonam:", 102, "Dhanbad")
    pickle.dump(stu, wf)
    pickle.dump(stu2, wf)
    print("Pickling Done...")

with open("student.dat", mode="rb") as rf:
    obj1 = pickle.load(rf)
    obj2 = pickle.load(rf)
    print("Unpickling Done...")

    """to display objects data"""
    obj1.disp()
    obj2.disp()