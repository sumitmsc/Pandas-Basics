import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Score": [85, 90, 95]
})

df.to_excel("output.xlsx", index=False)
print("Excel file generated: output.xlsx")
