# Financial Market Analysis with Machine Learning

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Ingridvasc/Portifolio/blob/main/LICENSE) 

This project uses advanced Machine Learning techniques to analyze historical financial market data and generate buy/sell signals. The code combines K-Means clustering, Hidden Markov Models (HMM), and neural networks to predict market trends.

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [🛠 Features](#-features)
- [🖥 Technologies Used](#-technologies-used)
- [📦 Prerequisites](#-prerequisites)
- [✏️ Author](#-author)

## 🌟 Overview <a name="-overview"></a>

This project aims to analyze historical price data of financial assets (e.g., stocks, cryptocurrencies) and generate buy/sell signals based on identified patterns. The process involves:

1. **Data Collection and Preprocessing**: Cleaning and preparing historical data.
2. **Candle Clustering**: Using K-Means to group candles into clusters.
3. **Hidden Markov Model (HMM)**: Identifying market states (uptrend, downtrend, consolidation).
4. **Neural Network**: Generating buy/sell signals based on clusters and trends.
5. **Model Evaluation**: Measuring the model's accuracy.
6. **Backtesting**: Testing the model on historical data to evaluate its effectiveness.

## 🛠 Features <a name="-features"></a>

- **Candle Clustering**: Grouping candles into clusters to identify patterns.
- **Trend Prediction**: Using HMM to predict market states.
- **Buy/Sell Signals**: Generating buy/sell signals using a neural network.
- **Backtesting**: Evaluating model performance on historical data.

## 🖥 Technologies Used <a name="-technologies-used"></a>

- **Python**: Main programming language.
- **Pandas**: Data manipulation.
- **NumPy**: Numerical computations.
- **Scikit-learn**: K-Means clustering and model evaluation.
- **hmmlearn**: Implementation of Hidden Markov Models.
- **TensorFlow/Keras**: Building and training neural networks.
- **TA-Lib**: Calculating technical indicators.

## 📦 Prerequisites <a name="-prerequisites"></a>

- Python 3.8 or higher.

## ✏️ Author <a name="-author"></a>

- [Ingrid Vasconcelos](https://github.com/Ingridvasc)
