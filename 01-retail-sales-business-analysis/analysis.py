import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('sales_data.csv')

# Basic cleaning
df.dropna(inplace=True)

# Revenue calculation
df['revenue'] = df['quantity'] * df['price']

# Group by category
category_sales = df.groupby('category')['revenue'].sum().sort_values(ascending=False)

print("Revenue by category:\n", category_sales)

# Plot
category_sales.plot(kind='bar')
plt.title('Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.show()