from tensorflow import keras
from tensorflow.keras.layers import LSTM, Dense, Embedding

# Hyperparameters 
max_sequence_length = 100  # Maximum length of a sequence
embedding_dim = 128  # Dimensionality of word embeddings
lstm_units = 256  # Number of units in the LSTM layer

# Define the model
model = keras.Sequential()
model.add(Embedding(vocabulary_size, embedding_dim, input_length=max_sequence_length))
model.add(LSTM(lstm_units, return_sequences=True))  # Allows for longer dependencies
model.add(LSTM(lstm_units))
model.add(Dense(vocabulary_size, activation='softmax'))  # Predict next word probability

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

