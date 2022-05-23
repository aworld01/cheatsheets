def exst(item):
    import os
    if not os.path.exists(item):
        os.makedirs(item)

exst('my_folder')