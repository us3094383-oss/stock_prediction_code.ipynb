# stock_prediction_code.ipynb
A Stock Prediction Model On Yahoo Finance Apple data.
# Stock Price Prediction using Linear Regression

#Overview#
This project predicts stock prices using historical data from Yahoo Finance.  
We use Linear Regression to model the relationship between stock features and closing prices.

(Tech Used)
Python
scikit-learn
yfinance
matplotlib

Dataset
Source: Yahoo Finance (`AAPL` - Apple Inc.)
Features: Open, High, Low, Volume
Target: Close

Steps
1. Import libraries
2. Download stock data using `yfinance`
3. Select features and target
4. Split data into train/test sets
5. Train Linear Regression model
6. Predict and visualize results

Results
The model predicts closing prices based on historical features.  
Below is a sample plot comparing **actual vs predicted** prices:

![Stock Prediction Plot](plot.png)

