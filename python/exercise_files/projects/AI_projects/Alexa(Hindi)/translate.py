import googletrans

def tran(text):
    gt=googletrans.Translator()
    t=gt.translate(text, src='en', dest='hi')
    data=t.text
    return data

if __name__ == "__main__":
    txt=tran("how are you")
    print(txt)
