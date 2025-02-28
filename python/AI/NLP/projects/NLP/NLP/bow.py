from tp import stem
import numpy as np

def BoW(tok,voc):
    sen = [stem(word) for word in tok]
    bag = np.zeros(len(voc),dtype=np.float32)
    for i,w in enumerate(voc):
        if w in sen:
            bag[i] = 1
    return bag

if __name__=="__main__":
    v = ['this','is','an','apple','red','green']
    t = ['this','is','a','mango','is','red','and','hi']

    print(BoW(t,v))