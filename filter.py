import pandas as pd

df = pd.read_csv("sample.csv")
filtered = df[df["age"] > 30]

print("Filtered Rows (age > 30):")
print(filtered)
