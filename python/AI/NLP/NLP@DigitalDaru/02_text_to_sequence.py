from tensorflow.keras.preprocessing.text import Tokenizer

sentences = ["I love my dog", "I love my cat", "Do you think my dog is amazing?"]
test = ["I love my amazing dog", "My cat love my dog"]

# token = Tokenizer(num_words=100) #to set limit of words (effects for .texts_to_sequences method)
token = Tokenizer()
token.fit_on_texts(sentences)
index = token.word_index
text_seq = token.texts_to_sequences(test) #match sequences of words

print(index)
print(text_seq)