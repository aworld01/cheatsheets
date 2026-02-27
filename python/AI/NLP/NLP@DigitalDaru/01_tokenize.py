from tensorflow.keras.preprocessing.text import Tokenizer

sentences = ["I love my dog", "I love my cat", "Do you think my dog is amazing?"]

token = Tokenizer() #to give number of uniqe words
token.fit_on_texts(sentences) #to fit text in tokenizer
index = token.word_index #to store words in index variable

print(index, type(index))