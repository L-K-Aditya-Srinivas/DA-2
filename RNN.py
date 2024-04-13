from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Hyperparameters (adjust based on your data)
max_len = 100  # Maximum sequence length
vocab_size = 10000  # Number of words to consider
embedding_dim = 128  # Dimensionality of word embeddings
lstm_units = 128  # Number of units in the LSTM layer


# Tokenize text data
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(texts)  # Replace 'texts' with your list of text reviews
sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, maxlen=max_len)

# Define labels (replace with 0 for negative, 1 for positive)
labels = [1 if sentiment == "positive" else 0 for sentiment in sentiments]  # Replace 'sentiments' with your sentiment labels

# Define the model
model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(LSTM(lstm_units))
model.add(Dense(1, activation='sigmoid'))  # Sigmoid for binary classification

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(padded_sequences, labels, epochs=10, validation_split=0.2)

# Evaluate the model (replace with your testing data)
test_sequences = tokenizer.texts_to_sequences(new_texts)  # Replace 'new_texts' with new reviews for testing
test_padded_sequences = pad_sequences(test_sequences, maxlen=max_len)
test_loss, test_acc = model.evaluate(test_padded_sequences, test_labels)  # Replace 'test_labels' with actual labels
print("Test Accuracy:", test_acc)

# Predict sentiment for new text (optional)
new_review = "This movie was fantastic!"
new_sequence = tokenizer.texts_to_sequences([new_review])
new_padded_sequence = pad_sequences(new_sequence, maxlen=max_len)
prediction = model.predict(new_padded_sequence)
sentiment = "positive" if prediction > 0.5 else "negative"
print("Predicted sentiment for new review:", sentiment)
