import os

class Replacer:
  def __init__(self, find, replace):
    self.find = find
    self.replace = replace
  def replace_one(self, file):
    count = 0
    with open(file, mode="r", encoding="utf-8") as rf:
      data = rf.read()
      count += data.count(self.find)
      repl = data.replace(self.find, self.replace)
      with open(file, mode="w", encoding="utf-8") as wf:
        wf.write(repl)
    print(f"Total records replaced: {count}")
  def replace_all(self, path):
    count = 0
    for paths, dirs, files in os.walk(path):
      for file in files:
        old = os.path.join(paths, file)
        if file == 'replacer.py':
          continue
        if os.path.isfile(old):

          with open(file, mode="r", encoding="utf-8") as rf:
            data = rf.read()
            count += data.count(self.find)
            repl = data.replace(self.find, self.replace)
            with open(old, mode="w", encoding="utf-8") as wf:
              wf.write(repl)
    print(f"Total records replaced: {count}")

if __name__ == "__main__":
  path = "."
  file = "test.txt"

  obj = Replacer("Abdul Zoha", "Hameed Hasan")

  # obj.replace_one(file)
  obj.replace_all(".")