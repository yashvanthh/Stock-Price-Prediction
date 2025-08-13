title: "Stock Price Prediction"
project_overview: |
  This project predicts future stock prices using Linear Regression on historical stock data.
  The dataset contains prices for multiple stocks (Stock_1 to Stock_5), and this version focuses on Stock_1.
  The model forecasts the stock price for the next 30 days and visualizes actual vs predicted values.

technologies_used:
  - Python 3
  - Pandas
  - NumPy
  - Matplotlib
  - Scikit-learn

dataset:
  format: "CSV"
  columns:
    - Date
    - Stock_1
    - Stock_2
    - Stock_3
    - Stock_4
    - Stock_5
  example: |
    2020-01-01,101.76,100.16,99.49,99.90,101.76
    2020-01-02,102.17,99.96,98.68,100.64,102.52

how_to_run: |
  1. Clone the repository:
     git clone https://github.com/<your-username>/stock-price-prediction.git
     cd stock-price-prediction
  2. Install dependencies:
     pip install pandas numpy scikit-learn matplotlib
  3. Place your dataset in the project folder as "stock_data.csv"
  4. Run the script:
     python stock_prediction.py

output: |
  - Displays the Mean Squared Error (MSE) of predictions
  - Shows a matplotlib graph comparing actual and predicted prices

future_improvements:
  - Add prediction for all 5 stocks automatically
  - Implement LSTM for better accuracy
  - Create a web interface for predictions

author:
  name: "Yashu M R"
  email: "your-email@example.com"
  github: "https://github.com/<your-username>"
