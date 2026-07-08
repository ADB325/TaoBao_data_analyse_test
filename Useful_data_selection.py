# 完整一键生成有效数据（带行号版）
import pandas as pd

df = pd.read_csv("user_behavior_processed.csv", encoding="utf-8")
df["原始行号"] = df.index

# 时间转换（替换列名）
df["time"] = pd.to_datetime(df["time"], errors="coerce")

# 排序 + 时间差
df = df.sort_values(["user_id", "item_category", "time"])
df["前向差"] = df.groupby(["user_id", "item_category"])["time"].diff()
df["后向差"] = df.groupby(["user_id", "item_category"])["time"].diff(-1).abs()

# 有效标记
window = pd.Timedelta(hours=144)
df["有效"] = (df["前向差"] <= window) | (df["后向差"] <= window)
df["有效"] = df["有效"].fillna(False)

# 提取有效行，恢复原始顺序
df_valid = df[df["有效"]].sort_values("原始行号").drop(columns=["原始行号","前向差","后向差","有效"])
df_valid.to_csv("Useful_data.csv", index=False, encoding="utf-8-sig")