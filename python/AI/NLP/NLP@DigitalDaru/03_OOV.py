from tensorflow.keras.preprocessing.text import Tokenizer

sentences = ["I love my dog", "I love my cat", "Do you think my dog is amazing?"]
test = ["I really love my dog", "My dog loves my manatee"]

"""Drop words"""
# token = Tokenizer(num_words=100) #to give number of uniqe words
# token.fit_on_texts(sentences) #to fit text in tokenizer
# index = token.word_index #to store words in index variable
# text_seq = token.texts_to_sequences(test)
# print(index)
# print(text_seq)


"""Fix drop words"""
token = Tokenizer(num_words=100, oov_token="<OVV>") #to give number of uniqe words
token.fit_on_texts(sentences) #to fit text in tokenizer
index = token.word_index #to store words in index variable
text_seq = token.texts_to_sequences(sentences)
print(index)
text_seq = token.texts_to_sequences(test)
print(text_seq)