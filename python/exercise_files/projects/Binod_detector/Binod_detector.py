import os
dir_contents = os.listdir()

# print(dir_contents) # print in one line

# # print in newline
# for item in dir_contents:
#     print(item)

# # # print only txt files.
# for item in dir_contents:
#     if item.endswith('txt'):
#         print(item)


def isBinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
    if "binod" in fileContent.lower():
        return True
    else:
        return False
    
# # for each text file, run isBinod in them...
if __name__ == "__main__":
    nBinod = 0
    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}")
            flag = isBinod(item)
            if (flag):
                print(f"Binod found in {item}")
                nBinod +=1
            else:
                print(f"Binod not found in {item}")
    print("*******Binod Detector Summary*******")
    print(f"{nBinod} files found with Binod hidden into them")