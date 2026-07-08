import pandas as pd

# ========== 1. 读取数据 ==========
# 根据你的实际情况，替换 '用户ID' '商品种类' '时间列' 这三个名字
df = pd.read_csv(
    "user_behavior_processed.csv",
    usecols=["user_id", "item_category", "time"],  # 只读必要的三列
    encoding="utf-8"
)

# 把时间列转成标准时间格式，报错就换 encoding="gbk"
df["time"] = pd.to_datetime(df["time"])

# ========== 2. 按用户和种类分组，对时间排序 ==========
df = df.sort_values(["user_id", "item_category", "time"])

# 计算每条记录与 前一条、后一条 的时间差（在同一用户-种类组内）
df["forward_difference"] = df.groupby(["user_id", "item_category"])["time"].diff()          # 与上一次的时间差
df["backward_difference"] = df.groupby(["user_id", "item_category"])["time"].diff(-1).abs() # 与下一次的时间差（取绝对值）

# ========== 3. 定义有效条件：前后7天(144小时)内至少有一次同类浏览 ==========
window = pd.Timedelta(hours=144)

# 前向差或后向差 ≤ 144小时 即认为有效（注意处理第一条/最后一条的空值，用False填充）
df["useful"] = (df["forward_difference"] <= window) | (df["backward_difference"] <= window)
df["useful"] = df["useful"].fillna(False)   # NaN（第一条的前向、最后一条的后向）视为不满足条件

# ========== 4. 分离出无效数据 ==========
invalid = df[~df["useful"]].drop(columns=["forward_difference", "backward_difference", "useful"])

# 保存结果
invalid.to_csv("Useless_data.csv", index=False, encoding="utf-8-sig")
print(f"原始总行数: {len(df)}")
print(f"无效数据行数: {len(invalid)}")
print("无效数据已保存到 Uesless_data.csv")