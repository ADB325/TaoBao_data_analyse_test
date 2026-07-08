# 用于检查数据集内时间是否正确
import pandas as pd
chunks = pd.read_csv('user_behavior_processed.csv', chunksize = 50000, usecols = ['time'])
error_indices = []
global_row_start = 0
for chunk in chunks:
    converted = pd.to_datetime(chunk['time'], format = '%Y-%m-%d %H', errors = 'coerce')
    mask = converted.isna()
    if mask.any():
        bad_rows = [global_row_start + i for i in chunk[mask].index]
        error_indices.extend(bad_rows)
    global_row_start += len(chunk)
if error_indices:
    print(f"❌ 发现 {len(error_indices)} 行时间格式异常：")
    print(f"异常行号（从0开始计数）：{error_indices[:20]}")  #只打印前20个
else:
    print("所有行的时间格式均正常。")
