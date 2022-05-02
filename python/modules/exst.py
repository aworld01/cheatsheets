import os
def exst(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)
exst('yourFolder')