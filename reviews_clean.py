import pandas as pd

reviews = pd.read_table('C:/Users/infin/Downloads/project_5/reviews.tsv')

# Replace data with easy to read format
reviews['last_review'] = pd.to_datetime(reviews['last_review'])
print(reviews.head())

# Save file as .csv
# reviews.to_csv('C:/Users/infin/Downloads/project_5/reviews.csv', index=False)
