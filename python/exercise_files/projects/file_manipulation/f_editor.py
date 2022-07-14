import os

from hamcrest import ends_with

class Editer:
    def __init__(self, path, find, replace, file_type):
        self.path = path
        self.find = find
        self.replace = replace
        self.file_type = file_type
    def modify(self):
        for file in os.listdir(self.path):
            if file == "f_editor.py":
                continue
            self.edit(file)
    def modify_bulk(self):
        for path, folders, files in os.walk(self.path):
            for new_file in files:
                if new_file == "f_editor.py":
                    continue
                file = os.path.join(path, new_file)
                self.edit(file)
    def edit(self, file):
        self.file = file
        if os.path.isfile(self.file) and file.endswith(self.file_type):
            with open(self.file, mode="r", encoding='utf-8') as rf:
                old_data = rf.read()
                new_data = old_data.replace(self.find, self.replace)
                with open(self.file, mode="w", encoding='utf-8') as wf:
                    wf.write(new_data)
                    """print updated data"""
                    if not new_data == old_data:
                        print(f"'{self.file}' is updated!")

if __name__ == "__main__":
    main_path = "."
    find_txt = ("World")
    replace_txt = "Abdul Zoha"
    f_type = "html"

    """creating object"""
    e = Editer(main_path, find_txt, replace_txt, f_type)
    """calling methods"""
    e.modify() #to change current dir files data
    # e.modify_bulk() #to change all files data in folder/subfolders
