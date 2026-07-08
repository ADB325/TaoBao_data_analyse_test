import pandas as pd
df = pd.read_csv('user_behavior_processed.csv')
print(df.head()) #数据导入和验证
import pandas as pd
chunk_size = 50000 #单次读取数量+定义chunk_size 也可以直接在chunks里边定义
chunks = pd.read_csv('user_behavior_processed.csv', chunksize=chunk_size)
unique_ids = set()
chunk_size = 50000
chunks = pd.read_csv('user_behavior_processed.csv', chunksize=chunk_size, usecols=['item_id']) #最后多出的部分用于锁定特定的列进行读取
for chunk in chunks: #不断拼凑的小组组合
    ids_in_this_chunk = chunk['item_id'].dropna().tolist()
    unique_ids.update(ids_in_this_chunk)
    print(len(unique_ids))
print(len(unique_ids))






