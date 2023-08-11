def checkFun(arg):
    return [i for i in dir(arg) if not "__" in i]

if __name__ == "__main__":
    emptyString = ""

    l = checkFun(emptyString)
    print(l)