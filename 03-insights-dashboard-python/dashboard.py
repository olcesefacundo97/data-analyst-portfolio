import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('clean_data.csv')

# KPI: total revenue
total_revenue = df['revenue'].sum()
print(f'Total Revenue: {total_revenue}')

# Revenue over time
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    revenue_trend = df.groupby('date')['revenue'].sum()
    revenue_trend.plot()
    plt.title('Revenue Over Time')
    plt.show()

# Top products
top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False).head(5)
top_products.plot(kind='bar')
plt.title('Top 5 Products')
plt.show()