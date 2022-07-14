import os

class Renamer:
    def __init__(self, path, ext, file_name):
        self.path = path
        self.ext = f".{ext}"
        self.file_name = file_name
        self.index = 1
    def modify(self):
        for file in os.listdir(self.path):
            if file == "renamer.py":
                continue
            self.renamer(file)
    def modify_bulk(self):
        for path, folders, files in os.walk(self.path):
            for new_file in files:
                if new_file == "renamer.py":
                    continue
                file = os.path.join(path, new_file)
                self.renamer(file)
    def renamer(self, file):
        if os.path.isfile(file):
            file2, extension = os.path.splitext(file)
            if extension == self.ext:
                new_name = f"{self.file_name}{self.index}{extension}"
                self.index += 1
                os.rename(file, new_name)

if __name__ == "__main__":
    main_path = "."
    ex = input("Enter extension: ")
    new_name = input("Enter the file name: ")
    ren = Renamer(main_path, ex, new_name)

    """calling methods"""
    ren.modify() #to change current dir files extension
    # ren.modify_bulk() #to change all files extension in folder/subfolders