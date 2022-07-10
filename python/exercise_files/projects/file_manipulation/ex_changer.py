import os

class Ex_changer:
    def __init__(self, path, old, new):
        self.path = path
        self.new_name = new
        self.old_name = old
    def modify(self):
        for file in os.listdir(self.path):
            if file == "modifier.py":
                continue
            self.extension_changer(file)
    def modify_bulk(self):
        for path, folders, files in os.walk(self.path):
            for new_file in files:
                if new_file == "modifier.py":
                    continue
                file = os.path.join(path, new_file)
                self.extension_changer(file)
    def extension_changer(self, file):
        self.path = file
        self.file, self.extension = os.path.splitext(self.path) #to split path
        if os.path.isfile(self.path) and (self.old_name in self.extension):
            new_name = f"{self.file}.{self.new_name}" #to generate new filename
            os.rename(self.path, new_name) #to rename file
        else:
            if os.path.isfile(self.path):
                print("Nothing to be changed...")

if __name__ == "__main__":
    main_path = "."
    find_txt = ("html")
    replace_txt = "txt"
    ex = Ex_changer(main_path, find_txt, replace_txt)

    """calling methods"""
    ex.modify() #to change current dir files extension
    # ex.modify_bulk() #to change all files extension in folder/subfolders