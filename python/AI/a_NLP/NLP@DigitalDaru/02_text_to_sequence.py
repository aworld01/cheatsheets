from tensorflow.keras.preprocessing.text import Tokenizer

sentences = ["I love my dog", "I love my cat", "Do you think my dog is amazing?"]
test = ["I love my amazing dog"]

token = Tokenizer(num_words=100) #to give number of uniqe words (necessary for .texts_to_sequences method)
token.fit_on_texts(sentences) #to fit text in tokenizer
index = token.word_index #to store words in index variable

text_seq = token.texts_to_sequences(test) #match sequences of words

print(index)
print(text_seq)