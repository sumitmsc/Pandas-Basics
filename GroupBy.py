import pandas as pd

df = pd.read_csv("sample.csv")
grouped = df.groupby("department")["salary"].mean()

print("Average Salary per Department:")
print(grouped)
