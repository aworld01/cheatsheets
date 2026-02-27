"""
{
    "editor.wordWrap": "on",
    "files.autoSave": "afterDelay",
    "liveServer.settings.donotShowInfoMsg": true,
    "workbench.startupEditor": "none",
    "[python]": {
        "editor.formatOnType": true
    },
    "git.openRepositoryInParentFolders": "never",
    "window.zoomLevel": 1,
    "workbench.colorTheme": "Monokai-Contrast",
    "editor.minimap.enabled": false,
    "notebook.output.textLineLimit": 300,
    "notebook.output.scrolling": true
}

Python          JSON Equivalent            
====            ===============
dict            object
list, tuple     array
str             string
int, float      number
True            true
False           false
None            null
"""
import json

file = "testDump.json"
list_data = ["Apple", "Orange", "Banana", "Guava"]
dict_data = {"name":"Abdul Zoha", "age":25, "skills":["python", "shell", "javaScript"], "Yes":True, "No":False}

with open(file, "w") as wf:
    # data = json.dump(data, wf) #to create json file
    data = json.dump(dict_data, wf, indent=4) #to give indent of 4 spaces