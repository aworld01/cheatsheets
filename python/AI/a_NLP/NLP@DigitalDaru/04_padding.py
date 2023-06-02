"""
padded = pad_sequences(sentences) #padding="pre" (default)
padded = pad_sequences(sentences, padding="post") #to add zeros at last
padded = pad_sequences(sentences, padding="post", maxlen=5) #to set a limit of padding
"""
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = ["I love my dog", "I love my cat", "Do you think my dog is amazing?"]
test = ["I love my amazing dog", "My cat love my dog and goat"]

token = Tokenizer(oov_token="OOV")
token.fit_on_texts(sentences)
word_index = token.word_index
sequences = token.texts_to_sequences(test)
padded = pad_sequences(sequences, padding="post") #to add zeros at last
shape = padded.shape

# print(word_index)
# print(len(word_index))

# print(sequences)

print(padded)
print(shape)