import pandas as pd

# Extract
raw = pd.read_csv('raw_data.csv')

# Transform
raw.dropna(inplace=True)
raw['revenue'] = raw['quantity'] * raw['price']

# Load
raw.to_csv('clean_data.csv', index=False)

print('Pipeline executed successfully')