import pandas as pd

price = pd.read_csv('C:/Users/infin/Downloads/project_5/prices.csv')

# get rid of dollars word and make price column in integer type
price['price'] = price['price'].str.strip('dollars')
price['price'] = price['price'].astype('int')

# sorting, removing outliers
price = price.sort_values(by=['price'], axis=0, ascending=False)
price = price[price['price'] < 4000]
price = price[price['price'] > 0]

print(price.head())

# Save changes
price.to_csv('C:/Users/infin/Downloads/project_5/prices.csv', index=False)
