#Project 1(Stock Prediction Using LinearRegression)

#Imports(Made)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import yfinance as yf

# Download Apple stock data
df = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
print(df.head())

#Dataset Configuration
X = df[['Open', 'High', 'Low', 'Volume']]
y = df['Close']

#Splitting the Dataset
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,shuffle=False)

#Model Settings
model=LinearRegression()

#Training The Model
model.fit(X_train,y_train)

#Plotting the Points
predictions = model.predict(X_test)
plt.figure(figsize=(10,6))
plt.plot(y_test.values, label="Actual")
plt.plot(predictions, label="Predicted")
plt.legend()
plt.show()
