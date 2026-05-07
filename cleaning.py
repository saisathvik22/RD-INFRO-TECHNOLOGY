import pandas as pd
df = pd.read_csv("data.csv")
df['date'] = pd.to_datetime(df['date'])
df['revenue'] = df['price'] * df['quantity']
print(df)