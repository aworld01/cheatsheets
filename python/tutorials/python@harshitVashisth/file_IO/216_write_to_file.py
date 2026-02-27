path = "files/file.txt"
with open(path, mode="r") as rf:
    with open("files/file2.txt", mode="w") as wf:
        wf.write(rf.read())