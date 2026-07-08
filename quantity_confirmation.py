import pandas as pd
df = pd.read_csv('user_behavior_processed.csv')
unique_users = set()
unique_items = set()
unique_categories = set()
chunks = pd.read_csv('user_behavior_processed.csv', chunksize = 50000, usecols =['user_id', 'item_id', 'item_category'])
for chunk in chunks:
    users = chunk['user_id'].dropna().tolist()
    unique_users.update(users)
    items = chunk['item_id'].dropna().tolist()
    unique_items.update(items)
    categories = chunk['item_category'].dropna().tolist()
    unique_categories.update(categories)
print({len(unique_users)})
print({len(unique_items)})
print({len(unique_categories)})
# 各自数据种类包含的商品数
