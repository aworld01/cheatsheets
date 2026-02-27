sub = {"name":"Abdul Zoha", "Fees":15000, "per":{"Python":5000,"JavaScript":5000, "Blender":5000}}

"""accessing each id key - value"""
for item in sub:
    if type(sub[item]) is dict:
        for item2 in sub[item]:
            print(f"{item2} = {sub[item][item2]}")
    else:
        print(f"{item} = {sub[item]}")