"""
A dictionary within another dictionary is called as nested dictionary or nesting of a dictionary.
Syntax:- nested_dict = {'Dict1': {'Key_A':'Value_A'},
                        'Dict2': {'Key_B':'Value_B'}
                        }
                                           
Creating empty nested dict
Syntax: - nested_dict = {'Dict1':{},
                         'Dict2':{}
                        }
"""

"""assigning a dictionary"""
sub = {
    "name":"Abdul Zoha",
    "Fees":15000, 
    "per": {"Python":5000,"JavaScript":5000, "Blender":5000}
    }
print(sub) #to access all items
print()


"""accessing nested dictionary """
# print(sub["name"]) #to print name
# print(sub["per"])



"""Modifying nested Dictionary"""
# sub["name"] = "Tabassum" #to modify value
# sub["per"]["Python"] = 20000 #to modify value
# print(sub)



"""Deleting nested Dictionary"""
# del sub["per"]["Python"] #to Delete item
# print(sub)



"""adding a new item"""
# sub["Duration"] = "2 Years" #to add item
# print(sub)



"""adding a dictionary into nested Dictionary"""
sub["Teachers"] = {"Parkash sir": "24 years", "Fatima madam": "36 years"} #to add a dictionary
print(sub)