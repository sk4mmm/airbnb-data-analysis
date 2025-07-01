import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs('visuals/charts', exist_ok=True)
df = pd.read_csv('../data/listings.csv.gz')

print(df.head())
print(df.info())
print(df.describe())

sns.set_style('whitegrid')
df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)

df = df.dropna(subset=['price'])

df_filtered = df[df['price'] < 500]
sns.histplot(df_filtered['price'], bins=100)

plt.title('Price Distribution of AirBnB in SA')
plt.xlabel('Price (€)')
plt.ylabel('Listings')
plt.savefig('visuals/charts/price_distribution.png')
plt.show()
