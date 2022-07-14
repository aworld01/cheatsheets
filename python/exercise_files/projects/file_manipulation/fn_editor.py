import os

class Editer:
    def __init__(self, path, find, replace, file_type):
        self.path = path
        self.find = find
        self.replace = replace
        self.file_type = file_type
    def modify(self):
        for file in os.listdir(self.path):
            if file == "fn_editor.py":
                continue
            self.edit(file)
    def modify_bulk(self):
        for path, folders, files in os.walk(self.path):
            for new_file in files:
                if new_file == "fn_editor.py":
                    continue
                file = os.path.join(path, new_file)
                self.edit(file)
    def edit(self, file):
        self.file = file
        if os.path.isfile(self.file) and file.endswith(self.file_type):
            file_name, extension = os.path.splitext(self.file)
            rep = file_name.replace(self.find, self.replace).lower()
            new_name = f"{rep}{extension}"
            if not self.file == new_name:
                os.rename(file, new_name)

if __name__ == "__main__":
    main_path = "."
    find_txt = ("document")
    replace_txt = "file"
    f_type = "txt"

    """creating object"""
    e = Editer(main_path, find_txt, replace_txt, f_type)
    """calling methods"""
    e.modify() #to change current dir files data
    # e.modify_bulk() #to change all files data in folder/subfolders