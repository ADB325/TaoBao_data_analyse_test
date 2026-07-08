import pandas as pd

# ==================== 配置区 ====================
INPUT_FILE = "Useful_data.csv"                  # 你已有的有效数据文件
OUTPUT_FILE = "Useful_data_clear_demostrate.csv"
# 根据你的数据列名修改（务必与文件实际表头一致）
COL_USER = "user_id"
COL_CATEGORY = "item_category"
COL_ITEM = "item_id"
COL_TIME = "time"
# ==============================================

# 1. 读取有效数据（不丢弃任何行）
df = pd.read_csv(INPUT_FILE, encoding="utf-8-sig")

# 2. 确保时间列是标准时间格式（如果你的时间已经是 "2025-11-01 10" 这样的字符串且可直接排序，此步可省略）
df[COL_TIME] = pd.to_datetime(df[COL_TIME])

# 3. 排序：按用户ID → 商品种类 → 商品ID → 时间
df_sorted = df.sort_values([COL_USER, COL_CATEGORY, COL_ITEM, COL_TIME])

# 4. 保存（保留所有列，不删除重复）
df_sorted.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print(f"原始有效数据行数: {len(df)}")
print(f"排序后行数（应与上相同）: {len(df_sorted)}")
print(f"文件已保存至: {OUTPUT_FILE}")