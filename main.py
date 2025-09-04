import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
dates = pd.date_range(start='2022-01-01', periods=365)
# Simulate website traffic with seasonality and a downward trend (churn)
trend = np.linspace(1000, 500, 365) # Linear decrease in traffic
seasonality = 100 * np.sin(2 * np.pi * np.arange(365) / 365) # Yearly seasonality
noise = 50 * np.random.randn(365) # Random noise
traffic = trend + seasonality + noise
df = pd.DataFrame({'Date': dates, 'Traffic': traffic})
df = df.set_index('Date')
# --- 2. Time Series Decomposition ---
decomposition = seasonal_decompose(df['Traffic'], model='additive', period=365)
# --- 3. Visualization and Saving ---
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(df['Traffic'], label='Original Traffic')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(decomposition.trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(decomposition.seasonal, label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(decomposition.resid, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()
output_filename = 'time_series_decomposition.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
# --- 4. Churn Prediction (Illustrative -  requires more sophisticated modeling for real-world application)---
#  This section provides a basic illustration.  A real-world application would require more robust forecasting techniques.
#  For example, using ARIMA, Prophet, or other time series forecasting models.
#Simple linear regression on the trend component to illustrate churn prediction.
#This is a highly simplified example and not a robust churn prediction model.
trend_df = pd.DataFrame({'Date':decomposition.trend.index, 'Trend':decomposition.trend.values})
trend_df['Time'] = range(len(trend_df))
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(trend_df[['Time']], trend_df['Trend'])
future_time = np.arange(len(trend_df), len(trend_df) + 30).reshape(-1,1) #predict next 30 days
predicted_trend = model.predict(future_time)
print("\nIllustrative Churn Prediction (Next 30 days):")
print(predicted_trend)
#Note: This is a highly simplified example.  Real-world churn prediction requires more sophisticated modeling.