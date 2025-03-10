# Importing libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from hmmlearn import hmm
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import talib  # For technical indicators

# 1. Data Collection and Preprocessing
# Example of historical data (replace with real data)
data = pd.read_csv('historical_data.csv')  # Expected columns: open, close, high, low

# Candle features
data['body'] = abs(data['close'] - data['open'])
data['upper_shadow'] = data['high'] - data[['open', 'close']].max(axis=1)
data['lower_shadow'] = data[['open', 'close']].min(axis=1) - data['low']
data['direction'] = np.where(data['close'] > data['open'], 1, 0)  # 1 = positive, 0 = negative

# Adding technical indicators (optional)
data['rsi'] = talib.RSI(data['close'], timeperiod=14)
data['macd'], data['macd_signal'], _ = talib.MACD(data['close'])

# Removing NaN values generated by indicators
data.dropna(inplace=True)

# 2. Candle Clustering
# Features for clustering
X = data[['body', 'upper_shadow', 'lower_shadow', 'direction']].values

# Clustering with K-Means
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X)
data['cluster'] = clusters

# 3. Hidden Markov Model (HMM)
# Preparing data for HMM
sequences = data['cluster'].values.reshape(-1, 1)

# Training the HMM
model_hmm = hmm.MultinomialHMM(n_components=3)  # 3 states: uptrend, downtrend, consolidation
model_hmm.fit(sequences)

# Example of probability predictions
probabilities = model_hmm.predict_proba(sequences)

# 4. Neural Network for Buy/Sell Signals
# Preparing data for the neural network
data['trend'] = np.where(data['close'].rolling(window=9).mean() > data['close'].rolling(window=21).mean(), 1, 0)  # 1 = uptrend, 0 = downtrend
X_nn = np.column_stack((clusters, data['trend'].shift(1).fillna(0)))  # Combining clusters and trends
y_nn = data['direction'].values  # Buy/sell signals (1 = buy, 0 = sell)

# Data normalization
scaler = StandardScaler()
X_nn = scaler.fit_transform(X_nn)

# Neural network
model_nn = Sequential()
model_nn.add(Dense(64, input_dim=X_nn.shape[1], activation='relu'))
model_nn.add(Dropout(0.2))  # Regularization to avoid overfitting
model_nn.add(Dense(32, activation='relu'))
model_nn.add(Dense(1, activation='sigmoid'))  # Binary output (buy/sell)
model_nn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Training the neural network
model_nn.fit(X_nn, y_nn, epochs=10, batch_size=32, validation_split=0.2)

# 5. Model Evaluation
# Neural network predictions
predictions = model_nn.predict(X_nn)

# Example of buy/sell signal
data['signal'] = np.where(predictions > 0.5, 1, 0)  # 1 = buy, 0 = sell

# Performance evaluation
accuracy = accuracy_score(y_nn, data['signal'])
print(f'Model accuracy: {accuracy * 100:.2f}%')

# 6. Backtesting (Optional)
# Splitting data into train and test sets
train_size = int(len(data) * 0.8)
train_data, test_data = data[:train_size], data[train_size:]

# Training the model on the training set
model_nn.fit(X_nn[:train_size], y_nn[:train_size], epochs=10, batch_size=32)

# Evaluating on the test set
test_predictions = model_nn.predict(X_nn[train_size:])
test_data['signal'] = np.where(test_predictions > 0.5, 1, 0)

# Calculating test accuracy
test_accuracy = accuracy_score(y_nn[train_size:], test_data['signal'])
print(f'Test accuracy: {test_accuracy * 100:.2f}%')

# 7. Example of Model Usage
# Generating a signal for the last candle
last_candle = X_nn[-1].reshape(1, -1)
last_candle_signal = model_nn.predict(last_candle)
print(f'Signal for the last candle: {"Buy" if last_candle_signal > 0.5 else "Sell"}')
