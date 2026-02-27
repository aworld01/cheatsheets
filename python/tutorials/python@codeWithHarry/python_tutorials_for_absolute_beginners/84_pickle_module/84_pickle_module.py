import pickle

"""pickling a python object"""
# cars = ["Audi", "PMW", "Maruti Suzuki", "Harryti Tuzuki", "Tesla"]
# file = "mycar.pkl"
# with open(file, "wb") as wf: #to create file object
#     pickle.dump(cars, wf)

"""unpickling a python object"""
file = "mycar.pkl"
with open(file, "rb") as rf:
    cars = pickle.load(rf)
print(cars)