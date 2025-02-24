import numpy as np

def bow(arg, voc):
   bag = np.zeros(len(voc), dtype=np.float32)
   for i,w in enumerate(arg):
      if w in voc:
         bag[i] = 1
   return bag

if __name__ == "__main__":
   v = ["This","is","an","apple","red","green"]
   t = ["This","is","a","mango","is","red","and","hi"]
   result = bow(t,v)
   print(result)