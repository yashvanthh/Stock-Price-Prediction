import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("stock_data.csv")
df = df[['Stock_1']]
forecast_out = 30
df['Prediction'] = df[['Stock_1']].shift(-forecast_out)
X = np.array(df.drop(['Prediction'], axis=1))
X = X[:-forecast_out]
y = np.array(df['Prediction'])
y = y[:-forecast_out]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")
x_future = df.drop(['Prediction'], axis=1)[-forecast_out:]
future_prediction = model.predict(np.array(x_future))
plt.figure(figsize=(10, 6))
plt.title("Stock Price Prediction for Stock_1")
plt.xlabel("Days")
plt.ylabel("Price")
plt.plot(df['Stock_1'], label="Actual Price")
future_index = range(len(df), len(df) + forecast_out)
plt.plot(future_index, future_prediction, label="Predicted Price", linestyle='--')
plt.legend()
plt.show()
